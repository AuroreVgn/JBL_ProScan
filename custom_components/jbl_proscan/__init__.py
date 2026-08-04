"""JBL ProScan integration."""

from __future__ import annotations

import asyncio
from datetime import timedelta

import voluptuous as vol

from homeassistant.config_entries import ConfigEntry, ConfigEntryState
from homeassistant.const import CONF_PASSWORD
from homeassistant.core import HomeAssistant, ServiceCall
from homeassistant.exceptions import ServiceValidationError
from homeassistant.helpers import config_validation as cv
from homeassistant.helpers.aiohttp_client import async_get_clientsession
from homeassistant.helpers import entity_registry as er
from homeassistant.util import slugify

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

SERVICE_REFRESH = "refresh"
ATTR_CONFIG_ENTRY_ID = "config_entry_id"


type JBLProScanConfigEntry = ConfigEntry[JBLProScanCoordinator]


async def async_setup(hass: HomeAssistant, config: dict) -> bool:
    """Set up the JBL ProScan integration and its services."""

    async def async_handle_refresh(call: ServiceCall) -> None:
        requested_entry_id = call.data.get(ATTR_CONFIG_ENTRY_ID)
        entries = [
            entry
            for entry in hass.config_entries.async_entries(DOMAIN)
            if entry.state is ConfigEntryState.LOADED
        ]

        if requested_entry_id:
            entries = [entry for entry in entries if entry.entry_id == requested_entry_id]
            if not entries:
                raise ServiceValidationError(
                    f"JBL ProScan configuration entry not found or not loaded: {requested_entry_id}"
                )

        if not entries:
            raise ServiceValidationError("No loaded JBL ProScan configuration entry")

        await asyncio.gather(
            *(entry.runtime_data.async_request_refresh() for entry in entries)
        )

    if not hass.services.has_service(DOMAIN, SERVICE_REFRESH):
        hass.services.async_register(
            DOMAIN,
            SERVICE_REFRESH,
            async_handle_refresh,
            schema=vol.Schema(
                {vol.Optional(ATTR_CONFIG_ENTRY_ID): cv.string},
                extra=vol.PREVENT_EXTRA,
            ),
        )

    return True


async def async_migrate_entry(hass: HomeAssistant, entry: JBLProScanConfigEntry) -> bool:
    """Migrate legacy JBL ProScan entities."""
    registry = er.async_get(hass)

    if entry.version < 3:
        for entity in er.async_entries_for_config_entry(registry, entry.entry_id):
            unique_id = entity.unique_id or ""
            if (
                unique_id.endswith("_numeric")
                or unique_id.endswith("_statistics")
                or unique_id.endswith("_measurement_count")
            ):
                registry.async_remove(entity.entity_id)

    if entry.version < 4:
        # Version 1.3.0 was missing the English runtime translation file.
        # Entities created with an English frontend could consequently receive
        # generic object IDs such as ``bassin`` or ``problem_2``. Give every
        # JBL binary sensor a stable and readable object ID.
        aquarium_slug = slugify(entry.title or "jbl_proscan")
        binary_sensor_ids = {
            "ph_ok": "ph_ok",
            "kh_ok": "kh_ok",
            "gh_ok": "gh_ok",
            "no2_high": "no2_high",
            "no3_high": "no3_high",
            "chlorine_high": "chlorine_high",
            "analysis_overdue": "analysis_overdue",
        }
        for entity in er.async_entries_for_config_entry(registry, entry.entry_id):
            if entity.domain != "binary_sensor":
                continue
            unique_id = entity.unique_id or ""
            key = next(
                (key for key in binary_sensor_ids if unique_id.endswith(f"_{key}")),
                None,
            )
            if key is None:
                continue
            new_entity_id = (
                f"binary_sensor.{aquarium_slug}_{binary_sensor_ids[key]}"
            )
            if entity.entity_id == new_entity_id:
                continue
            existing = registry.async_get(new_entity_id)
            if existing is None:
                registry.async_update_entity(
                    entity.entity_id, new_entity_id=new_entity_id
                )

        hass.config_entries.async_update_entry(entry, version=4)

    return True


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
