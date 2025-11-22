from __future__ import annotations

import pandas as pd

from modules.base_module import BaseModule
from core.session import Session
from .view import CargaDatosView


class CargaDatosController(BaseModule):
    def __init__(self, session: Session) -> None:
        super().__init__("carga_datos", "Carga de Datos", "📂")
        self.session = session
        self._view = CargaDatosView()
        self._connect_signals()

    def _connect_signals(self) -> None:
        self._view.load_button.clicked.connect(self._on_load_clicked)

    def view(self):
        return self._view

    def _on_load_clicked(self) -> None:
        file_path = self._view.ask_for_file()
        if not file_path:
            return

        result = self.session.get_data_service().load_csv(file_path)
        if not result.is_valid:
            self._view.render_preview("\n".join(result.errors))
            self._view.render_metadata(None)
            return

        metadata = self.session.get_data_service().get_data_metadata()
        preview = self._build_preview()
        self.session.set_loaded_file(file_path)
        self._view.render_metadata(metadata)
        self._view.render_preview(preview)

    def _build_preview(self) -> str:
        data = self.session.get_data_service().get_current_data()
        if data is None:
            return ""
        preview_df = data.head(5)
        return preview_df.to_markdown(index=False)

    def on_activate(self) -> None:
        metadata = self.session.get_data_service().get_data_metadata()
        self._view.render_metadata(metadata if metadata else None)
        if metadata:
            self._view.render_preview(self._build_preview())
