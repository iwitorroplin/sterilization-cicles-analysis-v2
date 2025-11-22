from __future__ import annotations

from PySide6.QtWidgets import QHBoxLayout, QWidget, QStackedWidget

from core.router import Router
from modules.base_module import BaseModule
from ui.sidebar import Sidebar
from ui.styles import app_stylesheet


class MainWindow(QWidget):
    def __init__(self, router: Router) -> None:
        super().__init__()
        self.router = router
        self._stack = QStackedWidget()
        self.sidebar = Sidebar()
        self._init_ui()
        self._connect_signals()

    def _init_ui(self) -> None:
        self.setStyleSheet(app_stylesheet())

        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        layout.addWidget(self.sidebar)
        layout.addWidget(self._stack, 1)

        self.sidebar.load_modules(list(self.router.registered_modules()))

    def _connect_signals(self) -> None:
        self.sidebar.module_selected.connect(self.router.navigate_to)

    def show_module(self, module: BaseModule) -> None:
        view = module.view()
        if self._stack.indexOf(view) == -1:
            self._stack.addWidget(view)
        self._stack.setCurrentWidget(view)
        self.sidebar.set_active(module.slug())
