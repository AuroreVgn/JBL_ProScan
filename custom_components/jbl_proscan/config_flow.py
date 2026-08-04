"""Config flow for JBL ProScan."""

from __future__ import annotations

from typing import Any

import voluptuous as vol

from homeassistant import config_entries
from homeassistant.const import CONF_PASSWORD
from homeassistant.core import callback
from homeassistant.data_entry_flow import FlowResult
from homeassistant.helpers.aiohttp_client import async_get_clientsession
from homeassistant.helpers.selector import (
    NumberSelector,
    NumberSelectorConfig,
    NumberSelectorMode,
    SelectSelector,
    SelectSelectorConfig,
    SelectSelectorMode,
)

from .api import JBLProScanApi
from .const import (
    CONF_AQUARIUM_ID,
    CONF_EMAIL,
    CONF_SCAN_INTERVAL,
    DEFAULT_SCAN_INTERVAL,
    DOMAIN,
    MAX_SCAN_INTERVAL,
    MIN_SCAN_INTERVAL,
)
from .exceptions import (
    JBLProScanAuthenticationError,
    JBLProScanConnectionError,
    JBLProScanParseError,
)


class JBLProScanConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a JBL ProScan config flow."""

    VERSION = 1

    def __init__(self) -> None:
        """Initialize the flow."""
        self._credentials: dict[str, Any] = {}
        self._aquariums: dict[str, str] = {}
        self._api: JBLProScanApi | None = None

    async def async_step_user(
        self, user_input: dict[str, Any] | None = None
    ) -> FlowResult:
        """Authenticate and discover the user's aquariums and ponds."""
        errors: dict[str, str] = {}

        if user_input is not None:
            api = JBLProScanApi(
                session=async_get_clientsession(self.hass),
                email=user_input[CONF_EMAIL],
                password=user_input[CONF_PASSWORD],
            )
            try:
                aquariums = await api.async_get_aquariums()
            except JBLProScanAuthenticationError:
                errors["base"] = "invalid_auth"
            except JBLProScanConnectionError:
                errors["base"] = "cannot_connect"
            except JBLProScanParseError:
                errors["base"] = "no_aquariums"
            except Exception:  # noqa: BLE001
                errors["base"] = "unknown"
            else:
                self._credentials = dict(user_input)
                self._aquariums = aquariums
                self._api = api
                return await self.async_step_aquarium()

        schema = vol.Schema(
            {
                vol.Required(CONF_EMAIL): str,
                vol.Required(CONF_PASSWORD): str,
                vol.Optional(
                    CONF_SCAN_INTERVAL, default=DEFAULT_SCAN_INTERVAL
                ): NumberSelector(
                    NumberSelectorConfig(
                        min=MIN_SCAN_INTERVAL,
                        max=MAX_SCAN_INTERVAL,
                        step=1,
                        mode=NumberSelectorMode.BOX,
                        unit_of_measurement="min",
                    )
                ),
            }
        )
        return self.async_show_form(
            step_id="user",
            data_schema=schema,
            errors=errors,
        )

    async def async_step_aquarium(
        self, user_input: dict[str, Any] | None = None
    ) -> FlowResult:
        """Let the user select one discovered aquarium or pond."""
        if not self._credentials or not self._aquariums or self._api is None:
            return self.async_abort(reason="discovery_expired")

        errors: dict[str, str] = {}
        if user_input is not None:
            aquarium_id = user_input[CONF_AQUARIUM_ID]
            if aquarium_id not in self._aquariums:
                errors["base"] = "invalid_aquarium"
            else:
                try:
                    data = await self._api.async_get_data(aquarium_id)
                except JBLProScanAuthenticationError:
                    errors["base"] = "invalid_auth"
                except JBLProScanConnectionError:
                    errors["base"] = "cannot_connect"
                except JBLProScanParseError:
                    errors["base"] = "invalid_aquarium"
                except Exception:  # noqa: BLE001
                    errors["base"] = "unknown"
                else:
                    await self.async_set_unique_id(
                        f"{self._credentials[CONF_EMAIL].lower()}_{aquarium_id}"
                    )
                    self._abort_if_unique_id_configured()
                    entry_data = {
                        **self._credentials,
                        CONF_AQUARIUM_ID: aquarium_id,
                    }
                    return self.async_create_entry(
                        title=data.aquarium_name,
                        data=entry_data,
                    )

        options = [
            {"value": aquarium_id, "label": name}
            for aquarium_id, name in self._aquariums.items()
        ]
        return self.async_show_form(
            step_id="aquarium",
            data_schema=vol.Schema(
                {
                    vol.Required(CONF_AQUARIUM_ID): SelectSelector(
                        SelectSelectorConfig(
                            options=options,
                            mode=SelectSelectorMode.DROPDOWN,
                        )
                    )
                }
            ),
            errors=errors,
        )

    @staticmethod
    @callback
    def async_get_options_flow(
        config_entry: config_entries.ConfigEntry,
    ) -> JBLProScanOptionsFlow:
        return JBLProScanOptionsFlow(config_entry)


class JBLProScanOptionsFlow(config_entries.OptionsFlow):
    """Handle JBL ProScan options."""

    def __init__(self, config_entry: config_entries.ConfigEntry) -> None:
        self._config_entry = config_entry

    async def async_step_init(
        self, user_input: dict[str, Any] | None = None
    ) -> FlowResult:
        if user_input is not None:
            return self.async_create_entry(title="", data=user_input)

        current = self._config_entry.options.get(
            CONF_SCAN_INTERVAL,
            self._config_entry.data.get(CONF_SCAN_INTERVAL, DEFAULT_SCAN_INTERVAL),
        )
        return self.async_show_form(
            step_id="init",
            data_schema=vol.Schema(
                {
                    vol.Required(
                        CONF_SCAN_INTERVAL, default=current
                    ): NumberSelector(
                        NumberSelectorConfig(
                            min=MIN_SCAN_INTERVAL,
                            max=MAX_SCAN_INTERVAL,
                            step=1,
                            mode=NumberSelectorMode.BOX,
                            unit_of_measurement="min",
                        )
                    )
                }
            ),
        )
