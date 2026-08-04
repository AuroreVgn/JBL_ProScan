"""Sensors for JBL ProScan."""

from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass
from datetime import datetime
import re
from typing import Any

from homeassistant.components.sensor import (
    SensorDeviceClass,
    SensorEntity,
    SensorEntityDescription,
    SensorStateClass,
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
    DOMAIN,
    HISTORY_LIMIT,
)
from .coordinator import JBLProScanCoordinator
from .models import JBLMeasurement, JBLProScanData

INTEGRATION_VERSION = "1.3.0"
ATTR_COMPARATOR = "comparator"
ATTR_DISPLAY_VALUE = "display_value"
ATTR_NUMERIC_VALUE_NOTE = "numeric_value_note"


def _parse_numeric(raw: str | None) -> float | None:
    """Extract the numeric boundary from a JBL value."""
    if raw is None:
        return None
    match = re.match(r"^\s*([<>]=?)?\s*(-?\d+(?:[.,]\d+)?)", str(raw))
    if not match:
        return None
    return float(match.group(2).replace(",", "."))


def _comparator(raw: str | None) -> str:
    """Return the optional comparator from a JBL value."""
    if raw is None:
        return ""
    match = re.match(r"^\s*([<>]=?)?", str(raw))
    return (match.group(1) or "") if match else ""


@dataclass(frozen=True, kw_only=True)
class JBLProScanSensorDescription(SensorEntityDescription):
    """Describe a JBL ProScan sensor."""

    value_fn: Callable[[JBLProScanData], Any]
    raw_key: str | None = None


MEASUREMENT_SENSORS: tuple[JBLProScanSensorDescription, ...] = (
    JBLProScanSensorDescription(
        key="ph", translation_key="ph", icon="mdi:ph",
        state_class=SensorStateClass.MEASUREMENT,
        suggested_display_precision=2,
        value_fn=lambda d: _parse_numeric(d.latest.ph), raw_key="ph",
    ),
    JBLProScanSensorDescription(
        key="kh", translation_key="kh", icon="mdi:water-outline",
        native_unit_of_measurement="°dKH",
        state_class=SensorStateClass.MEASUREMENT,
        suggested_display_precision=1,
        value_fn=lambda d: _parse_numeric(d.latest.kh), raw_key="kh",
    ),
    JBLProScanSensorDescription(
        key="gh", translation_key="gh", icon="mdi:water-opacity",
        native_unit_of_measurement="°dGH",
        state_class=SensorStateClass.MEASUREMENT,
        suggested_display_precision=1,
        value_fn=lambda d: _parse_numeric(d.latest.gh), raw_key="gh",
    ),
    JBLProScanSensorDescription(
        key="no2", translation_key="no2", icon="mdi:alert-decagram-outline",
        native_unit_of_measurement="mg/L",
        state_class=SensorStateClass.MEASUREMENT,
        suggested_display_precision=2,
        value_fn=lambda d: _parse_numeric(d.latest.no2), raw_key="no2",
    ),
    JBLProScanSensorDescription(
        key="no3", translation_key="no3", icon="mdi:leaf-circle-outline",
        native_unit_of_measurement="mg/L",
        state_class=SensorStateClass.MEASUREMENT,
        suggested_display_precision=1,
        value_fn=lambda d: _parse_numeric(d.latest.no3), raw_key="no3",
    ),
    JBLProScanSensorDescription(
        key="co2", translation_key="co2", icon="mdi:molecule-co2",
        native_unit_of_measurement="mg/L",
        state_class=SensorStateClass.MEASUREMENT,
        suggested_display_precision=1,
        value_fn=lambda d: _parse_numeric(d.latest.co2), raw_key="co2",
    ),
    JBLProScanSensorDescription(
        key="chlorine", translation_key="chlorine", icon="mdi:flask-outline",
        native_unit_of_measurement="mg/L",
        state_class=SensorStateClass.MEASUREMENT,
        suggested_display_precision=2,
        value_fn=lambda d: _parse_numeric(d.latest.chlorine), raw_key="chlorine",
    ),
)

SENSORS: tuple[JBLProScanSensorDescription, ...] = (
    *MEASUREMENT_SENSORS,
    JBLProScanSensorDescription(
        key="last_analysis", translation_key="last_analysis",
        icon="mdi:calendar-clock", device_class=SensorDeviceClass.TIMESTAMP,
        value_fn=lambda d: d.latest.measured_at,
    ),
    JBLProScanSensorDescription(
        key="history", translation_key="history",
        icon="mdi:chart-timeline-variant", value_fn=lambda d: d.measurement_count,
    ),
)


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry[JBLProScanCoordinator],
    async_add_entities: AddConfigEntryEntitiesCallback,
) -> None:
    """Set up JBL ProScan sensors."""
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
        self._entry_id = entry.entry_id
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
    def native_value(self) -> int | float | datetime | None:
        """Return the native sensor value."""
        value = self.entity_description.value_fn(self.coordinator.data)
        if isinstance(value, datetime):
            return _aware_datetime(value)
        return value

    @property
    def extra_state_attributes(self) -> dict[str, Any] | None:
        """Return additional attributes."""
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
                "config_entry_id": self._entry_id,
                "integration_version": INTEGRATION_VERSION,
                "measurement_units": {
                    "ph": None,
                    "kh": "°dKH",
                    "gh": "°dGH",
                    "no2": "mg/L",
                    "no3": "mg/L",
                    "co2": "mg/L",
                    "chlorine": "mg/L",
                },
            }

        if description.key == "last_analysis":
            return None

        latest = self.coordinator.data.latest
        raw_value = getattr(latest, description.raw_key) if description.raw_key else None
        comparator = _comparator(raw_value)
        attrs: dict[str, Any] = {
            "aquarium_id": self.coordinator.data.aquarium_id,
            "measurement_key": description.key,
            "config_entry_id": self._entry_id,
            ATTR_RAW_VALUE: raw_value,
            ATTR_DISPLAY_VALUE: raw_value,
            ATTR_COMPARATOR: comparator,
            ATTR_SOURCE: latest.source,
            ATTR_MEASUREMENT_ID: latest.measurement_id,
            ATTR_MEASUREMENT_DATE: _aware_datetime(latest.measured_at).isoformat(),
        }
        if comparator:
            attrs[ATTR_NUMERIC_VALUE_NOTE] = (
                "The numeric state is the JBL boundary value. "
                "The original comparison is retained in raw_value and comparator."
            )
        return attrs
