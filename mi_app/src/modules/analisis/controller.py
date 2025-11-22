from __future__ import annotations

import pandas as pd

from modules.base_module import BaseModule
from core.session import Session
from .view import AnalisisView


class AnalisisController(BaseModule):
    def __init__(self, session: Session) -> None:
        super().__init__("analisis", "Análisis", "📈")
        self.session = session
        self._view = AnalisisView()

    def view(self):
        return self._view

    def on_activate(self) -> None:
        data = self.session.get_data_service().get_current_data()
        summary: dict[str, str] = {}

        if data is not None:
            summary["Filas"] = str(len(data))
            summary["Columnas"] = str(len(data.columns))
            numeric_cols = data.select_dtypes(include=["number"])
            if not numeric_cols.empty:
                summary["Promedio global"] = f"{numeric_cols.mean().mean():.2f}"
                summary["Desviación global"] = f"{numeric_cols.std().mean():.2f}"
            summary["Columnas numéricas"] = ", ".join(numeric_cols.columns) if not numeric_cols.empty else "-"
        self._view.render_summary(summary)
