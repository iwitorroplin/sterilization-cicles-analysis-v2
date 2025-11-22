from __future__ import annotations

from typing import Any, Dict


# ruta de los archivos json para almacenar
from pathlib import Path

"""
BASE_DIR = Path(__file__).resolve().parent.parent.parent
SRC_DIR = BASE_DIR / "src"
DATA_DIR = BASE_DIR / "data"

# config
CONFIG_DIR = SRC_DIR / "config"
APP_CONFIG_PATH = CONFIG_DIR / "app_config.json""
"""


class AppSettings:
    """Almacena configuración global de la aplicación."""

    _basic_config: Dict[str, Any] = {}

    @classmethod
    def set_basic_config(cls, config: Dict[str, Any]):
        cls._basic_config = config or {}

    @classmethod
    def get_basic_config(cls) -> Dict[str, Any]:
        return cls._basic_config
