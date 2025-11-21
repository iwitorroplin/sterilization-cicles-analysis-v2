from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget, QTabWidget

from src.style import Style
from .tabs.general_tab import GeneralTab
# from .tabs.programs_tab import ProgramsTab

class ModuleView(QWidget):
    def __init__(self):
        super().__init__()
        self._build_ui()

    def _build_ui(self):
        layout = QVBoxLayout()
        layout.setContentsMargins(24, 24, 24, 24)
        layout.setSpacing(12)

        title = QLabel("Configuración")
        Style.label.title(title)
        title.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)

        # QTabWidget
        self.tabs = QTabWidget()
        self.tabs.setTabPosition(QTabWidget.North)
        self.tabs.setMovable(False)
        self.tabs.setDocumentMode(False)

        # Añadir pestañas desde clases separadas
        self.tabs.addTab(GeneralTab(), "General")

        # self.tabs.addTab(ProgramsTab(), "PROGRAMAS")

        layout.addWidget(title)
        layout.addWidget(self.tabs)
        Style.tab.apply(self.tabs)


        self.setLayout(layout)
        Style.widget.apply(self)
