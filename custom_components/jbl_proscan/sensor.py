"""Sensors for JBL ProScan."""

from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass
from datetime import datetime
from typing import Any

from homeassistant.components.sensor import (
    SensorDeviceClass,
    SensorEntity,
    SensorEntityDescription,
)
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.device_registry import DeviceInfo
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity
from homeassistant.util import dt as dt_util

from .const import (
    ATTR_MEASUREMENT_DATE,
    ATTR_MEASUREMENT_ID,
    ATTR_MEASUREMENTS,
    ATTR_RAW_VALUE,
    ATTR_SOURCE,
    ATTR_UNIT_HINT,
    DOMAIN,
    HISTORY_LIMIT,
)
from .coordinator import JBLProScanCoordinator
from .models import JBLMeasurement, JBLProScanData

INTEGRATION_VERSION = "1.0.0"


@dataclass(frozen=True, kw_only=True)
class JBLProScanSensorDescription(SensorEntityDescription):
    """Describe a JBL ProScan sensor."""

    value_fn: Callable[[JBLProScanData], Any]
    unit_hint: str | None = None


SENSORS: tuple[JBLProScanSensorDescription, ...] = (
    JBLProScanSensorDescription(key="ph", translation_key="ph", icon="mdi:ph", value_fn=lambda d: d.latest.ph),
    JBLProScanSensorDescription(key="kh", translation_key="kh", icon="mdi:water-percent", value_fn=lambda d: d.latest.kh, unit_hint="°dKH"),
    JBLProScanSensorDescription(key="gh", translation_key="gh", icon="mdi:water-percent", value_fn=lambda d: d.latest.gh, unit_hint="°dGH"),
    JBLProScanSensorDescription(key="no2", translation_key="no2", icon="mdi:flask", value_fn=lambda d: d.latest.no2, unit_hint="mg/L"),
    JBLProScanSensorDescription(key="no3", translation_key="no3", icon="mdi:flask", value_fn=lambda d: d.latest.no3, unit_hint="mg/L"),
    JBLProScanSensorDescription(key="co2", translation_key="co2", icon="mdi:molecule-co2", value_fn=lambda d: d.latest.co2, unit_hint="mg/L"),
    JBLProScanSensorDescription(key="chlorine", translation_key="chlorine", icon="mdi:chemical-weapon", value_fn=lambda d: d.latest.chlorine, unit_hint="mg/L"),
    JBLProScanSensorDescription(
        key="last_analysis",
        translation_key="last_analysis",
        icon="mdi:calendar-clock",
        device_class=SensorDeviceClass.TIMESTAMP,
        value_fn=lambda d: d.latest.measured_at,
    ),
    JBLProScanSensorDescription(
        key="measurement_count",
        translation_key="measurement_count",
        icon="mdi:counter",
        value_fn=lambda d: d.measurement_count,
    ),
    JBLProScanSensorDescription(
        key="history",
        translation_key="history",
        icon="mdi:chart-timeline-variant",
        value_fn=lambda d: d.measurement_count,
    ),
)


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry[JBLProScanCoordinator],
    async_add_entities: AddConfigEntryEntitiesCallback,
) -> None:
    coordinator = entry.runtime_data
    async_add_entities(
        JBLProScanSensor(coordinator, entry, description) for description in SENSORS
    )


def _aware_datetime(value: datetime) -> datetime:
    """Return a timezone-aware UTC datetime."""
    if value.tzinfo is None:
        value = value.replace(tzinfo=dt_util.DEFAULT_TIME_ZONE)
    return dt_util.as_utc(value)


def _measurement_to_dict(measurement: JBLMeasurement) -> dict[str, str]:
    """Serialize a measurement for state attributes and Lovelace cards."""
    return {
        "id": measurement.measurement_id,
        "date": _aware_datetime(measurement.measured_at).isoformat(),
        "source": measurement.source,
        "ph": measurement.ph,
        "kh": measurement.kh,
        "gh": measurement.gh,
        "no2": measurement.no2,
        "no3": measurement.no3,
        "co2": measurement.co2,
        "chlorine": measurement.chlorine,
    }


class JBLProScanSensor(CoordinatorEntity[JBLProScanCoordinator], SensorEntity):
    """Representation of a JBL ProScan sensor."""

    _attr_has_entity_name = True

    def __init__(
        self,
        coordinator: JBLProScanCoordinator,
        entry: ConfigEntry,
        description: JBLProScanSensorDescription,
    ) -> None:
        super().__init__(coordinator)
        self.entity_description = description
        self._attr_unique_id = f"{coordinator.data.aquarium_id}_{description.key}"
        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, coordinator.data.aquarium_id)},
            name=coordinator.data.aquarium_name,
            manufacturer="JBL",
            model="ProScan",
            configuration_url=(
                "https://www.jbl.de/fr/useraquarium/detail/"
                f"{coordinator.data.aquarium_id}/mes-analyses?country=fr"
            ),
        )

    @property
    def native_value(self) -> str | int | datetime | None:
        value = self.entity_description.value_fn(self.coordinator.data)
        if isinstance(value, datetime):
            return _aware_datetime(value)
        return value

    @property
    def extra_state_attributes(self) -> dict[str, Any] | None:
        description = self.entity_description

        if description.key == "history":
            measurements = self.coordinator.data.measurements[-HISTORY_LIMIT:]
            return {
                ATTR_MEASUREMENTS: [
                    _measurement_to_dict(measurement) for measurement in measurements
                ],
                "returned_measurements": len(measurements),
                "total_measurements": self.coordinator.data.measurement_count,
                "aquarium_id": self.coordinator.data.aquarium_id,
                "aquarium_name": self.coordinator.data.aquarium_name,
                "integration_version": INTEGRATION_VERSION,
            }

        if description.key in ("last_analysis", "measurement_count"):
            return None

        latest = self.coordinator.data.latest
        attrs: dict[str, Any] = {
            ATTR_RAW_VALUE: description.value_fn(self.coordinator.data),
            ATTR_SOURCE: latest.source,
            ATTR_MEASUREMENT_ID: latest.measurement_id,
            ATTR_MEASUREMENT_DATE: _aware_datetime(latest.measured_at).isoformat(),
        }
        if description.unit_hint:
            attrs[ATTR_UNIT_HINT] = description.unit_hint
        return attrs
