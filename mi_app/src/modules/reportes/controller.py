from __future__ import annotations

from modules.base_module import BaseModule
from core.session import Session
from .view import ReportesView


class ReportesController(BaseModule):
    def __init__(self, session: Session) -> None:
        super().__init__("reportes", "Reportes", "📝")
        self.session = session
        self._view = ReportesView()
        self._view.generate_button.clicked.connect(self._generate_stub)

    def view(self):
        return self._view

    def _generate_stub(self) -> None:
        metadata = self.session.get_data_service().get_data_metadata()
        if not metadata:
            message = "Carga datos para generar un resumen en PDF."
        else:
            message = (
                "Reporte listo para generarse.\n"
                f"Archivo: {metadata.get('file_path')}\n"
                f"Filas: {metadata.get('rows')} | Columnas: {len(metadata.get('columns', []))}"
            )
        self._view.render_report_message(message)
