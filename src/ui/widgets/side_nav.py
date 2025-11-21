from PySide6.QtCore import Signal
from PySide6.QtWidgets import QLabel, QMessageBox, QPushButton, QVBoxLayout, QWidget

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

    def add_module(self, module_name: str, icon_text: str = "» "):
        """Añade un módulo al sidebar."""
        btn = QPushButton(f"{icon_text} {module_name}")
        Style.button.primary(btn)
        btn.clicked.connect(lambda: self._on_navigation_selected(module_name))

        # Insertar antes del stretch
        self.layout().insertWidget(self.layout().count() - 1, btn)
        self.buttons[module_name] = btn

    def add_exit_action(self, icon_text: str = "⎋ "):
        """Añade el botón de salida al sidebar."""
        exit_label = "Salir"
        btn = QPushButton(f"{icon_text} {exit_label}")
        Style.button.exit(btn)
        btn.setCheckable(False)
        btn.clicked.connect(lambda: self._on_navigation_selected(exit_label))

        self.layout().insertWidget(self.layout().count() - 1, btn)
        self.buttons[exit_label] = btn

    def _on_navigation_selected(self, option: str):
        """Maneja la selección de navegación"""
        if option == "Salir":
            reply = QMessageBox.question(
                self,
                "Confirmar salida",
                "¿Deseas salir de la aplicación?",
                QMessageBox.Yes | QMessageBox.No
            )
            if reply == QMessageBox.Yes:
                self.window().close()
            return

        self._activate_button(option)
        self.module_changed.emit(option)

    def _activate_button(self, selected: str):
        """Activa visualmente el botón seleccionado (excepto Salir)"""
        for name, btn in self.buttons.items():
            if name == "Salir":
                btn.setChecked(False)
            else:
                previous_state = btn.blockSignals(True)
                btn.setChecked(name == selected)
                btn.blockSignals(previous_state)
                if name == selected:
                    self.current_button = btn

    def highlight_module(self, module_name: str):
        """Marca el módulo como activo sin volver a emitir señales."""
        if module_name not in self.buttons:
            return

        self._activate_button(module_name)

    def set_active_module(self, module_name: str):
        if module_name == "Salir":
            return

        self.highlight_module(module_name)
        self.module_changed.emit(module_name)
