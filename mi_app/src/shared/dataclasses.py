from __future__ import annotations

from dataclasses import dataclass, asdict, field
from typing import Any, Dict, List


@dataclass
class GeneralConfig:
    printer: str
    data_ferlo_dir: str
    raw_data_ferlo_dir: str
    process_data_ferlo_dir: str

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class CycleDetectorConfig:
    temperature: float
    auto: bool
    bad_value: str

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class AppConfig:
    general: GeneralConfig
    cycle_detector: CycleDetectorConfig

    def to_dict(self) -> Dict[str, Any]:
        return {
            "general": self.general.to_dict(),
            "cycle_detector": self.cycle_detector.to_dict(),
        }


@dataclass
class ProgramConfig:
    program_id: int
    program_name: str
    product_name: str
    format: str
    target_time: float
    target_temperature: float
    enabled: bool

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class ProgramsConfig:
    programs: List[ProgramConfig]

    def to_dict(self) -> Dict[str, Any]:
        return {"programs": [program.to_dict() for program in self.programs]}


@dataclass
class ValidationResult:
    is_valid: bool
    errors: List[str] = field(default_factory=list)

    def add_error(self, error: str) -> None:
        self.errors.append(error)
        self.is_valid = False
