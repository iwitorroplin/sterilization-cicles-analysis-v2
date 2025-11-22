from __future__ import annotations

from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import QLabel, QTabWidget, QVBoxLayout, QWidget

from src.style import Style
from .tabs.general_tab import GeneralTab
from .tabs.programs_tab import ProgramsTab


class ConfigView(QWidget):
    """Vista de configuración organizada en pestañas."""

    config_updated = Signal(str, dict)  # section, payload
    program_added = Signal(dict)
    program_deleted = Signal(int)

    def __init__(self) -> None:
        super().__init__()

        self.general_tab = GeneralTab()
        self.programs_tab = ProgramsTab()

        self._build_ui()
        self._connect_signals()

    def _build_ui(self) -> None:
        layout = QVBoxLayout(self)
        layout.setContentsMargins(24, 24, 24, 24)
        layout.setSpacing(12)

        title = QLabel("Configuración")
        Style.label.title(title)
        title.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)

        self.tabs = QTabWidget()
        self.tabs.setTabPosition(QTabWidget.North)
        self.tabs.addTab(self.general_tab, "General")
        self.tabs.addTab(self.programs_tab, "Programas")
        Style.tab.apply(self.tabs)

        layout.addWidget(title)
        layout.addWidget(self.tabs)
        Style.widget.apply(self)

    def _connect_signals(self) -> None:
        self.general_tab.general_saved.connect(
            lambda payload: self.config_updated.emit("general", payload)
        )
        self.general_tab.detector_saved.connect(
            lambda payload: self.config_updated.emit("cycle_detector", payload)
        )
        self.programs_tab.program_added.connect(self.program_added.emit)
        self.programs_tab.program_deleted.connect(self.program_deleted.emit)

    def load_app_config(self, app_config) -> None:
        self.general_tab.load_app_config(app_config)

    def load_programs(self, programs) -> None:
        self.programs_tab.load_programs(programs)

    def clear_program_form(self) -> None:
        self.programs_tab.clear_program_form()
