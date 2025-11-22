from __future__ import annotations

from PySide6.QtWidgets import QMainWindow

from core.router import Router
from core.session import Session
from ui.main_window import MainWindow


class Application(QMainWindow):
    """Ventana principal de la app y punto de unión del router."""

    def __init__(self, router: Router, session: Session) -> None:
        super().__init__()
        self.router = router
        self.session = session

        self.setWindowTitle("Análisis de ciclos de esterilización")
        self.setGeometry(100, 100, 1400, 900)

        self.main_window = MainWindow(router)
        self.setCentralWidget(self.main_window)

        self.router.module_changed.connect(self._on_module_changed)

    def _on_module_changed(self, module_name: str) -> None:
        self.session.set_current_module(module_name)
        module = self.router.get(module_name)
        self.main_window.show_module(module)
        module.on_activate()
