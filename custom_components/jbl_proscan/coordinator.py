"""Data update coordinator for JBL ProScan."""

from __future__ import annotations

from datetime import timedelta
import logging

from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, UpdateFailed

from .api import JBLProScanApi
from .exceptions import JBLProScanError
from .models import JBLProScanData

_LOGGER = logging.getLogger(__name__)


class JBLProScanCoordinator(DataUpdateCoordinator[JBLProScanData]):
    """Coordinate updates from JBL."""

    config_entry: ConfigEntry

    def __init__(
        self,
        hass: HomeAssistant,
        config_entry: ConfigEntry,
        api: JBLProScanApi,
        update_interval: timedelta,
    ) -> None:
        super().__init__(
            hass,
            _LOGGER,
            config_entry=config_entry,
            name="JBL ProScan",
            update_interval=update_interval,
        )
        self.api = api

    async def _async_update_data(self) -> JBLProScanData:
        try:
            return await self.api.async_get_data()
        except JBLProScanError as err:
            raise UpdateFailed(str(err)) from err
