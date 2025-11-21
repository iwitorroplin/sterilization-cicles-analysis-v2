from PySide6.QtCore import Signal
from PySide6.QtWidgets import QLabel, QPushButton, QVBoxLayout, QWidget

from src.style import Style
from src.core.config import SIDEBAR_WIDTH


class SidebarWidget(QWidget):
    module_changed = Signal(str)

    def __init__(self):
        super().__init__()
        self.current_button = None
        self.buttons = {}
        self._build_sidebar()

    def _build_sidebar(self):
        """Construye el sidebar."""
        self.setFixedWidth(SIDEBAR_WIDTH)

        layout = QVBoxLayout()
        layout.setContentsMargins(5, 10, 5, 10)
        layout.setSpacing(8)

        title = QLabel("Navegación")
        Style.label.title(title)
        layout.addWidget(title)

        layout.addStretch()
        self.setLayout(layout)
        Style.widget.apply(self)

    def add_module(self, module_name: str, icon_text: str = "»"):
        """Añade un módulo al sidebar."""
        btn = QPushButton(f"{icon_text} {module_name}")
        btn.setCheckable(True)
        btn.clicked.connect(lambda: self._on_module_clicked(module_name, btn))

        # Insertar antes del stretch
        self.layout().insertWidget(self.layout().count() - 1, btn)
        self.buttons[module_name] = btn

    def _on_module_clicked(self, module_name: str, button: QPushButton):
        """Maneja el clic en un módulo."""
        self.highlight_module(module_name)
        self.module_changed.emit(module_name)

    def highlight_module(self, module_name: str):
        """Marca el módulo como activo sin volver a emitir señales."""
        if module_name not in self.buttons:
            return

        button = self.buttons[module_name]
        if self.current_button and self.current_button is not button:
            self.current_button.setChecked(False)

        self.current_button = button
        previous_state = button.blockSignals(True)
        button.setChecked(True)
        button.blockSignals(previous_state)

    def set_active_module(self, module_name: str):
        self.highlight_module(module_name)
        self.module_changed.emit(module_name)
