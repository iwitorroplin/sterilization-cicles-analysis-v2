from __future__ import annotations

from typing import Any, Dict


class AppSettings:
    """Almacena configuración global de la aplicación."""

    _basic_config: Dict[str, Any] = {}

    @classmethod
    def set_basic_config(cls, config: Dict[str, Any]):
        cls._basic_config = config or {}

    @classmethod
    def get_basic_config(cls) -> Dict[str, Any]:
        return cls._basic_config
