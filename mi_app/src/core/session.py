from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from shared.services.config_service import ConfigService
from shared.services.data_service import DataService


@dataclass
class SessionState:
    current_module: Optional[str] = None
    last_loaded_file: Optional[str] = None
    data_preview: Optional[str] = None


class Session:
    """Singleton ligero que comparte servicios y estado transversal."""

    _instance: "Session" | None = None

    def __new__(cls) -> "Session":
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self) -> None:
        if self._initialized:
            return

        self.config_service = ConfigService()
        self.data_service = DataService()
        self.state = SessionState()

        self._initialized = True

    def get_config_service(self) -> ConfigService:
        return self.config_service

    def get_data_service(self) -> DataService:
        return self.data_service

    def set_current_module(self, module_name: str) -> None:
        self.state.current_module = module_name

    def set_loaded_file(self, file_path: Optional[str]) -> None:
        self.state.last_loaded_file = file_path
