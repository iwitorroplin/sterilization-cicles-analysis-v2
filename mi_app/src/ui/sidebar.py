from __future__ import annotations

from typing import Iterable
from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QButtonGroup, QLabel, QFrame
from PySide6.QtCore import Qt, Signal

from modules.base_module import BaseModule
from ui.styles import palette


class Sidebar(QWidget):
    module_selected = Signal(str)

    def __init__(self) -> None:
        super().__init__()
        self._button_group = QButtonGroup()
        self._button_group.setExclusive(True)
        self._buttons: dict[str, QPushButton] = {}
        self._init_ui()

    def _init_ui(self) -> None:
        self.setFixedWidth(240)
        layout = QVBoxLayout(self)
        layout.setContentsMargins(16, 24, 16, 24)
        layout.setSpacing(12)

        title = QLabel("Analítica de ciclos")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("font-size: 16px; font-weight: 700; color: %s;" % palette.SECONDARY)
        layout.addWidget(title)

        separator = QFrame()
        separator.setFrameShape(QFrame.HLine)
        separator.setFrameShadow(QFrame.Sunken)
        layout.addWidget(separator)

        self._modules_container = QVBoxLayout()
        self._modules_container.setSpacing(8)
        layout.addLayout(self._modules_container)
        layout.addStretch()

    def load_modules(self, modules: Iterable[BaseModule]) -> None:
        for module in modules:
            button = QPushButton(module.title())
            button.setCheckable(True)
            button.setProperty("module_slug", module.slug())
            button.clicked.connect(lambda checked, slug=module.slug(): self.module_selected.emit(slug))
            button.setStyleSheet(
                """
                QPushButton {
                    text-align: left;
                    padding: 10px 12px;
                    border-radius: 8px;
                    background: transparent;
                    color: %s;
                }
                QPushButton:hover { background: %s; }
                QPushButton:checked { background: %s; color: white; font-weight: 600; }
                """
                % (palette.TEXT, palette.BORDER, palette.PRIMARY)
            )

            self._button_group.addButton(button)
            self._buttons[module.slug()] = button
            self._modules_container.addWidget(button)

    def set_active(self, module_slug: str) -> None:
        button = self._buttons.get(module_slug)
        if button:
            button.setChecked(True)
