"""HTTP client and HTML parser for JBL ProScan."""

from __future__ import annotations

import asyncio
from datetime import datetime
from html.parser import HTMLParser
import logging
import re
from typing import Any

from aiohttp import ClientError, ClientSession, ClientTimeout

from .const import (
    ANALYSES_URL,
    AQUARIUMS_URL,
    BASE_URL,
    DEFAULT_TIMEOUT,
    LOGIN_PAGE,
    LOGIN_VERIFY,
    USER_INFO,
)
from .exceptions import (
    JBLProScanAuthenticationError,
    JBLProScanConnectionError,
    JBLProScanParseError,
)
from .models import JBLMeasurement, JBLProScanData

_LOGGER = logging.getLogger(__name__)


class _AnalysesHTMLParser(HTMLParser):
    """Small dependency-free parser for the JBL analyses table."""

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.in_h2 = False
        self.h2_parts: list[str] = []
        self.aquarium_name = "JBL ProScan"
        self.in_table = False
        self.in_tbody = False
        self.in_tr = False
        self.in_td = False
        self.current_cell: list[str] = []
        self.current_row: list[str] = []
        self.rows: list[list[str]] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attrs_dict = dict(attrs)
        if tag == "h2" and not self.rows:
            self.in_h2 = True
            self.h2_parts = []
        elif tag == "table" and "responsive" in (attrs_dict.get("class") or ""):
            self.in_table = True
        elif tag == "tbody" and self.in_table:
            self.in_tbody = True
        elif tag == "tr" and self.in_tbody:
            self.in_tr = True
            self.current_row = []
        elif tag == "td" and self.in_tr:
            self.in_td = True
            self.current_cell = []

    def handle_data(self, data: str) -> None:
        if self.in_h2:
            self.h2_parts.append(data)
        if self.in_td:
            self.current_cell.append(data)

    def handle_endtag(self, tag: str) -> None:
        if tag == "h2" and self.in_h2:
            name = " ".join("".join(self.h2_parts).split())
            if name:
                self.aquarium_name = name
            self.in_h2 = False
        elif tag == "td" and self.in_td:
            value = " ".join("".join(self.current_cell).split())
            self.current_row.append(value)
            self.in_td = False
        elif tag == "tr" and self.in_tr:
            if self.current_row:
                self.rows.append(self.current_row)
            self.in_tr = False
        elif tag == "tbody" and self.in_tbody:
            self.in_tbody = False
        elif tag == "table" and self.in_table:
            self.in_table = False


def parse_analyses_html(html: str, aquarium_id: str) -> JBLProScanData:
    """Parse the JBL analyses page and return all measurements."""
    parser = _AnalysesHTMLParser()
    parser.feed(html)

    measurements: list[JBLMeasurement] = []
    for row in parser.rows:
        # Expected columns: ID, Date, Source, pH, KH, GH, NO2, NO3, CO2, Cl, action
        if len(row) < 10:
            continue
        measurement_id, date_raw, source, ph, kh, gh, no2, no3, co2, chlorine = row[:10]
        try:
            measured_at = datetime.strptime(date_raw, "%d.%m.%Y %H:%M")
        except ValueError:
            _LOGGER.debug("Skipping JBL row with invalid date: %s", row)
            continue
        measurements.append(
            JBLMeasurement(
                measurement_id=measurement_id,
                measured_at=measured_at,
                source=source,
                ph=ph,
                kh=kh,
                gh=gh,
                no2=no2,
                no3=no3,
                co2=co2,
                chlorine=chlorine,
            )
        )

    if not measurements:
        raise JBLProScanParseError("No JBL ProScan measurements found in the page")

    latest = max(measurements, key=lambda item: item.measured_at)
    return JBLProScanData(
        aquarium_id=aquarium_id,
        aquarium_name=parser.aquarium_name,
        measurement_count=len(measurements),
        latest=latest,
        measurements=tuple(sorted(measurements, key=lambda item: item.measured_at)),
    )


class JBLProScanApi:
    """Client for the myJBL website."""

    def __init__(
        self,
        session: ClientSession,
        email: str,
        password: str,
        aquarium_id: str | None = None,
    ) -> None:
        self._session = session
        self._email = email
        self._password = password
        self._aquarium_id = aquarium_id
        self._authenticated = False

    async def async_login(self) -> None:
        """Authenticate against myJBL."""
        timeout = ClientTimeout(total=DEFAULT_TIMEOUT)
        try:
            async with self._session.get(
                f"{BASE_URL}{LOGIN_PAGE}", timeout=timeout
            ) as response:
                response.raise_for_status()
                login_html = await response.text()

            csrf_match = re.search(
                r'name=["\']csrf_token["\'][^>]*value=["\']([^"\']*)',
                login_html,
                flags=re.IGNORECASE,
            )
            csrf_token = csrf_match.group(1) if csrf_match else ""

            async with self._session.post(
                f"{BASE_URL}{LOGIN_VERIFY}",
                data={
                    "csrf_token": csrf_token,
                    "user": self._email,
                    "password": self._password,
                },
                headers={"Referer": f"{BASE_URL}{LOGIN_PAGE}"},
                allow_redirects=True,
                timeout=timeout,
            ) as response:
                response.raise_for_status()
                await response.read()

            async with self._session.get(
                f"{BASE_URL}{USER_INFO}", timeout=timeout
            ) as response:
                if response.status in (401, 403):
                    raise JBLProScanAuthenticationError("Invalid myJBL credentials")
                response.raise_for_status()
                try:
                    payload: dict[str, Any] = await response.json(content_type=None)
                except (ValueError, TypeError) as err:
                    raise JBLProScanAuthenticationError(
                        "Unable to validate the myJBL session"
                    ) from err

            if not payload.get("success"):
                raise JBLProScanAuthenticationError("Invalid myJBL credentials")

            self._authenticated = True
        except JBLProScanAuthenticationError:
            self._authenticated = False
            raise
        except (ClientError, asyncio.TimeoutError) as err:
            self._authenticated = False
            raise JBLProScanConnectionError(str(err)) from err

    async def async_get_aquariums(self) -> dict[str, str]:
        """Discover aquariums and ponds available in the myJBL account."""
        if not self._authenticated:
            await self.async_login()

        timeout = ClientTimeout(total=DEFAULT_TIMEOUT)
        url = f"{BASE_URL}{AQUARIUMS_URL}"
        try:
            async with self._session.get(url, timeout=timeout) as response:
                response.raise_for_status()
                html = await response.text()
        except (ClientError, asyncio.TimeoutError) as err:
            raise JBLProScanConnectionError(str(err)) from err

        if 'id="login-form"' in html or "app-name-login" in html:
            self._authenticated = False
            await self.async_login()
            async with self._session.get(url, timeout=timeout) as response:
                response.raise_for_status()
                html = await response.text()

        aquarium_ids = list(dict.fromkeys(re.findall(
            r'href=["\'][^"\']*/useraquarium/detail/(\d+)/[^"\']*["\']',
            html,
            flags=re.IGNORECASE,
        )))
        if not aquarium_ids:
            raise JBLProScanParseError("No aquariums or ponds found")

        aquariums: dict[str, str] = {}
        for aquarium_id in aquarium_ids:
            detail_url = f"{BASE_URL}{ANALYSES_URL.format(aquarium_id=aquarium_id)}"
            try:
                async with self._session.get(detail_url, timeout=timeout) as response:
                    response.raise_for_status()
                    detail_html = await response.text()
            except (ClientError, asyncio.TimeoutError) as err:
                _LOGGER.warning(
                    "Unable to read JBL aquarium %s during discovery: %s",
                    aquarium_id,
                    err,
                )
                continue

            parser = _AnalysesHTMLParser()
            parser.feed(detail_html)
            name = parser.aquarium_name
            if name == "JBL ProScan":
                name = f"JBL ProScan ({aquarium_id})"
            # Include the ID to disambiguate identically named basins.
            aquariums[aquarium_id] = f"{name} — {aquarium_id}"

        if not aquariums:
            raise JBLProScanParseError("Unable to read discovered aquariums")
        return aquariums

    async def async_get_data(self, aquarium_id: str | None = None) -> JBLProScanData:
        """Return all available ProScan values for one aquarium or pond."""
        if not self._authenticated:
            await self.async_login()

        timeout = ClientTimeout(total=DEFAULT_TIMEOUT)
        selected_id = aquarium_id or self._aquarium_id
        if not selected_id:
            raise JBLProScanParseError("No aquarium selected")
        url = f"{BASE_URL}{ANALYSES_URL.format(aquarium_id=selected_id)}"
        try:
            async with self._session.get(url, timeout=timeout) as response:
                if response.status in (401, 403):
                    self._authenticated = False
                    await self.async_login()
                    return await self.async_get_data(selected_id)
                response.raise_for_status()
                html = await response.text()
        except (ClientError, asyncio.TimeoutError) as err:
            raise JBLProScanConnectionError(str(err)) from err

        # JBL redirects expired sessions to the login page with HTTP 200.
        if 'id="login-form"' in html or "app-name-login" in html:
            self._authenticated = False
            await self.async_login()
            async with self._session.get(url, timeout=timeout) as response:
                response.raise_for_status()
                html = await response.text()

        return parse_analyses_html(html, selected_id)
