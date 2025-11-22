from dataclasses import dataclass
from typing import List

@dataclass
class ProgramFormData:
    program_id: int = 0
    program_name: str = ""
    product_name: str = ""
    format: str = ""
    target_time: float = 50.0
    target_temperature: float = 110.0
    enabled: bool = True
    
    def to_dict(self):
        return {
            "program_id": self.program_id,
            "program_name": self.program_name,
            "product_name": self.product_name,
            "format": self.format,
            "target_time": self.target_time,
            "target_temperature": self.target_temperature,
            "enabled": self.enabled
        }