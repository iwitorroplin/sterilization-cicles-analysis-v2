from __future__ import annotations

from dataclasses import dataclass


@dataclass
class ProgramFormData:
    program_id: int = 0
    program_name: str = ""
    product_name: str = ""
    format: str = ""
    target_time: float = 0.0
    target_temperature: float = 0.0
    enabled: bool = True

    def to_dict(self) -> dict:
        return {
            "program_id": self.program_id,
            "program_name": self.program_name,
            "product_name": self.product_name,
            "format": self.format,
            "target_time": self.target_time,
            "target_temperature": self.target_temperature,
            "enabled": self.enabled,
        }
