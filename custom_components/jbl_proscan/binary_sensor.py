"""Binary sensors for JBL ProScan water quality."""

from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass
from datetime import datetime, timezone
import re
from typing import Any

from homeassistant.components.binary_sensor import (
    BinarySensorDeviceClass,
    BinarySensorEntity,
    BinarySensorEntityDescription,
)
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.device_registry import DeviceInfo
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .const import CONF_REMINDER_DAYS, DEFAULT_REMINDER_DAYS, DOMAIN
from .coordinator import JBLProScanCoordinator
from .models import JBLProScanData


def _number(raw: str | None) -> tuple[float | None, str]:
    if raw is None:
        return None, ""
    match = re.match(r"^\s*([<>]=?)?\s*(-?\d+(?:[.,]\d+)?)", str(raw))
    if not match:
        return None, ""
    return float(match.group(2).replace(",", ".")), match.group(1) or ""


def _between(raw: str | None, low: float, high: float) -> bool | None:
    value, comparator = _number(raw)
    if value is None:
        return None
    if comparator.startswith(">") and value >= high:
        return False
    if comparator.startswith("<") and value <= low:
        return False
    return low <= value <= high


def _above(raw: str | None, threshold: float) -> bool | None:
    value, comparator = _number(raw)
    if value is None:
        return None
    if comparator.startswith(">"):
        return value >= threshold
    if comparator.startswith("<"):
        return False if value <= threshold else None
    return value > threshold


@dataclass(frozen=True, kw_only=True)
class JBLBinarySensorDescription(BinarySensorEntityDescription):
    value_fn: Callable[[JBLProScanData, int], bool | None]
    threshold_label: str


BINARY_SENSORS: tuple[JBLBinarySensorDescription, ...] = (
    JBLBinarySensorDescription(
        key="ph_ok", translation_key="ph_ok", icon="mdi:ph",
        value_fn=lambda d, _: _between(d.latest.ph, 6.5, 8.5),
        threshold_label="6.5–8.5",
    ),
    JBLBinarySensorDescription(
        key="kh_ok", translation_key="kh_ok", icon="mdi:water-outline",
        value_fn=lambda d, _: _between(d.latest.kh, 5, 15),
        threshold_label="5–15 °dKH",
    ),
    JBLBinarySensorDescription(
        key="gh_ok", translation_key="gh_ok", icon="mdi:water-opacity",
        value_fn=lambda d, _: _between(d.latest.gh, 4, 21),
        threshold_label="4–21 °dGH",
    ),
    JBLBinarySensorDescription(
        key="no2_high", translation_key="no2_high", icon="mdi:alert-decagram-outline",
        device_class=BinarySensorDeviceClass.PROBLEM,
        value_fn=lambda d, _: _above(d.latest.no2, 0.25),
        threshold_label="> 0.25 mg/L",
    ),
    JBLBinarySensorDescription(
        key="no3_high", translation_key="no3_high", icon="mdi:leaf-circle-outline",
        device_class=BinarySensorDeviceClass.PROBLEM,
        value_fn=lambda d, _: _above(d.latest.no3, 50),
        threshold_label="> 50 mg/L",
    ),
    JBLBinarySensorDescription(
        key="chlorine_high", translation_key="chlorine_high", icon="mdi:flask-outline",
        device_class=BinarySensorDeviceClass.PROBLEM,
        value_fn=lambda d, _: _above(d.latest.chlorine, 0.8),
        threshold_label="> 0.8 mg/L",
    ),
    JBLBinarySensorDescription(
        key="analysis_overdue", translation_key="analysis_overdue",
        icon="mdi:calendar-alert", device_class=BinarySensorDeviceClass.PROBLEM,
        value_fn=lambda d, days: (datetime.now(timezone.utc) - (d.latest.measured_at if d.latest.measured_at.tzinfo else d.latest.measured_at.replace(tzinfo=timezone.utc))).days >= days,
        threshold_label="configurable",
    ),
)


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry[JBLProScanCoordinator],
    async_add_entities: AddConfigEntryEntitiesCallback,
) -> None:
    coordinator = entry.runtime_data
    async_add_entities(
        JBLProScanBinarySensor(coordinator, entry, description)
        for description in BINARY_SENSORS
    )


class JBLProScanBinarySensor(CoordinatorEntity[JBLProScanCoordinator], BinarySensorEntity):
    _attr_has_entity_name = True

    def __init__(self, coordinator: JBLProScanCoordinator, entry: ConfigEntry, description: JBLBinarySensorDescription) -> None:
        super().__init__(coordinator)
        self.entity_description = description
        self._entry = entry
        self._attr_unique_id = f"{coordinator.data.aquarium_id}_{description.key}"
        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, coordinator.data.aquarium_id)},
            name=coordinator.data.aquarium_name, manufacturer="JBL", model="ProScan",
        )

    @property
    def is_on(self) -> bool | None:
        days = int(
            self._entry.options.get(
                CONF_REMINDER_DAYS,
                self._entry.data.get(CONF_REMINDER_DAYS, DEFAULT_REMINDER_DAYS),
            )
        )
        return self.entity_description.value_fn(self.coordinator.data, days)

    @property
    def extra_state_attributes(self) -> dict[str, Any]:
        latest = self.coordinator.data.latest
        attrs: dict[str, Any] = {
            "aquarium_id": self.coordinator.data.aquarium_id,
            "measurement_date": latest.measured_at.isoformat(),
            "recommended_threshold": self.entity_description.threshold_label,
        }
        if self.entity_description.key == "analysis_overdue":
            attrs["reminder_days"] = int(
                self._entry.options.get(
                    CONF_REMINDER_DAYS,
                    self._entry.data.get(CONF_REMINDER_DAYS, DEFAULT_REMINDER_DAYS),
                )
            )
        return attrs
