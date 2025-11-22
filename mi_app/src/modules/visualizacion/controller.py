from __future__ import annotations

from modules.base_module import BaseModule
from core.session import Session
from .view import VisualizacionView


class VisualizacionController(BaseModule):
    def __init__(self, session: Session) -> None:
        super().__init__("visualizacion", "Visualización", "📊")
        self.session = session
        self._view = VisualizacionView()

    def view(self):
        return self._view
