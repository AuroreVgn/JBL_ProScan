"""JBL ProScan integration."""

from __future__ import annotations

from datetime import timedelta

from homeassistant.config_entries import ConfigEntry
from homeassistant.const import CONF_PASSWORD
from homeassistant.core import HomeAssistant
from homeassistant.helpers.aiohttp_client import async_get_clientsession

from .api import JBLProScanApi
from .const import (
    CONF_AQUARIUM_ID,
    CONF_EMAIL,
    CONF_SCAN_INTERVAL,
    DEFAULT_SCAN_INTERVAL,
    DOMAIN,
    PLATFORMS,
)
from .coordinator import JBLProScanCoordinator


type JBLProScanConfigEntry = ConfigEntry[JBLProScanCoordinator]


async def async_setup_entry(hass: HomeAssistant, entry: JBLProScanConfigEntry) -> bool:
    """Set up JBL ProScan from a config entry."""
    session = async_get_clientsession(hass)
    api = JBLProScanApi(
        session=session,
        email=entry.data[CONF_EMAIL],
        password=entry.data[CONF_PASSWORD],
        aquarium_id=entry.data[CONF_AQUARIUM_ID],
    )
    interval_minutes = entry.options.get(
        CONF_SCAN_INTERVAL,
        entry.data.get(CONF_SCAN_INTERVAL, DEFAULT_SCAN_INTERVAL),
    )
    coordinator = JBLProScanCoordinator(
        hass,
        entry,
        api,
        timedelta(minutes=interval_minutes),
    )
    await coordinator.async_config_entry_first_refresh()
    entry.runtime_data = coordinator
    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)
    entry.async_on_unload(entry.add_update_listener(_async_reload_entry))
    return True


async def async_unload_entry(hass: HomeAssistant, entry: JBLProScanConfigEntry) -> bool:
    """Unload a config entry."""
    return await hass.config_entries.async_unload_platforms(entry, PLATFORMS)


async def _async_reload_entry(hass: HomeAssistant, entry: JBLProScanConfigEntry) -> None:
    """Reload when options change."""
    await hass.config_entries.async_reload(entry.entry_id)
