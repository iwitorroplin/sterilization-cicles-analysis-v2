from __future__ import annotations

from pathlib import Path
from typing import Dict, Optional

import pandas as pd

from ..dataclasses import ValidationResult


class DataService:
    _instance: "DataService" | None = None

    def __new__(cls) -> "DataService":
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self) -> None:
        if self._initialized:
            return

        self._current_data: Optional[pd.DataFrame] = None
        self._current_file: Optional[Path] = None
        self._data_metadata: Dict[str, object] = {}
        self._initialized = True

    def load_csv(self, file_path: str) -> ValidationResult:
        result = ValidationResult(is_valid=True)
        path = Path(file_path)
        if not path.exists():
            result.add_error("El archivo no existe")
            return result

        try:
            data = pd.read_csv(path, sep=",", encoding="utf-8", low_memory=False)
        except Exception as exc:  # pragma: no cover - errores de IO
            result.add_error(f"No se pudo leer el archivo: {exc}")
            return result

        if data.empty:
            result.add_error("El CSV está vacío")
            return result

        self._current_data = data
        self._current_file = path
        self._data_metadata = {
            "file_path": str(path),
            "rows": len(data),
            "columns": list(data.columns),
        }
        return result

    def get_current_data(self) -> Optional[pd.DataFrame]:
        return self._current_data

    def get_data_metadata(self) -> Dict[str, object]:
        return dict(self._data_metadata)

    def clear(self) -> None:
        self._current_data = None
        self._current_file = None
        self._data_metadata = {}
