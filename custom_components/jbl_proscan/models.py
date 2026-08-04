"""Data models for JBL ProScan."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime


@dataclass(slots=True, frozen=True)
class JBLMeasurement:
    """One JBL ProScan measurement."""

    measurement_id: str
    measured_at: datetime
    source: str
    ph: str
    kh: str
    gh: str
    no2: str
    no3: str
    co2: str
    chlorine: str


@dataclass(slots=True, frozen=True)
class JBLProScanData:
    """Data returned by JBL."""

    aquarium_id: str
    aquarium_name: str
    measurement_count: int
    latest: JBLMeasurement
    measurements: tuple[JBLMeasurement, ...]
