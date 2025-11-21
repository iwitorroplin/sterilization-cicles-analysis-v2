from PySide6.QtWidgets import (
    QWidget,
    QDialog,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QCheckBox,
    QPushButton,
    QSizePolicy
)

from src.core.config import (
    MODAL_MIN_WIDTH,
    MODAL_MIN_HEIGHT
)
from src.style import Style


class ProgramDialog(QDialog):
    """Ventana modular para añadir o editar un programa."""

    def __init__(self, parent=None, program=None):
        super().__init__(parent)

        self.setMinimumSize(MODAL_MIN_WIDTH, MODAL_MIN_HEIGHT)
        self.setWindowTitle("Editar Programa" if program else "Nuevo Programa")

        self.program = program if program else {
            "program_id": None,
            "program_name": "",
            "product_name": "",
            "format": "",
            "target_time": 60,
            "target_temperature": 110,
            "enabled": True,
        }

        self._setup_ui()

    def _setup_ui(self):
        layout = QVBoxLayout()
        main_layout_config = Style.layout.main()
        layout.setContentsMargins(*main_layout_config["margins"])
        layout.setSpacing(main_layout_config["spacing"])

        work_area_layout = QVBoxLayout()
        work_area_layout.setContentsMargins(0, 0, 0, 0)
        work_area_layout.setSpacing(Style.config.Layout.MAIN_SPACING)

        # ÁREAS EN ORDEN
        work_area_layout.addWidget(self._create_id_area())
        work_area_layout.addWidget(self._create_name_area())
        work_area_layout.addWidget(self._create_product_area())
        work_area_layout.addWidget(self._create_format_area())
        work_area_layout.addWidget(self._create_time_area())
        work_area_layout.addWidget(self._create_temp_area())
        work_area_layout.addWidget(self._create_enabled_area())

        work_area_layout.addStretch()
        work_area_layout.addWidget(self._create_button_area())

        layout.addLayout(work_area_layout)
        self.setLayout(layout)
        Style.widget.apply(self)

    def _create_id_area(self):
        container = QWidget()
        container.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(Style.config.Layout.BUTTON_SPACING)

        lbl = QLabel("ID Programa:")
        lbl.setFixedWidth(140)
        self.id_label = QLabel(str(self.program["program_id"]) if self.program["program_id"] else "—")

        layout.addWidget(lbl)
        layout.addWidget(self.id_label)
        
        Style.label.apply(lbl,"normal")

        container.setLayout(layout)
        return container

    def _create_name_area(self):
        container = QWidget()
        container.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(Style.config.Layout.BUTTON_SPACING)

        lbl = QLabel("Nombre Programa:")
        lbl.setFixedWidth(140)
        self.name_edit = QLineEdit(self.program["program_name"])

        layout.addWidget(lbl)
        layout.addWidget(self.name_edit)
        Style.label.apply(lbl,"normal")
        Style.input.apply(self.name_edit)
        
        container.setLayout(layout)
        return container

    def _create_product_area(self):
        container = QWidget()
        container.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(Style.config.Layout.BUTTON_SPACING)

        lbl = QLabel("Nombre Producto:")
        lbl.setFixedWidth(140)
        self.product_edit = QLineEdit(self.program["product_name"])



        layout.addWidget(lbl)
        layout.addWidget(self.product_edit)
        Style.label.apply(lbl,"normal")
        Style.input.apply(self.product_edit)

        container.setLayout(layout)
        return container
    
    def _create_format_area(self):
        container = QWidget()
        container.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(Style.config.Layout.BUTTON_SPACING)

        lbl = QLabel("Formato:")
        lbl.setFixedWidth(140)
        self.format_edit = QLineEdit(self.program["format"])

        layout.addWidget(lbl)
        layout.addWidget(self.format_edit)
        Style.label.apply(lbl,"normal")
        Style.input.apply(self.format_edit)
        
        container.setLayout(layout)
        return container
    
    def _create_time_area(self):
        container = QWidget()
        container.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(Style.config.Layout.BUTTON_SPACING)

        lbl = QLabel("Tiempo (min):")
        lbl.setFixedWidth(140)
        self.time_edit = QLineEdit(str(self.program["target_time"]))
        self.time_edit.setPlaceholderText("Ej: 60")

        layout.addWidget(lbl)
        layout.addWidget(self.time_edit)
        Style.label.apply(lbl,"normal")
        Style.input.apply(self.time_edit)
        
        container.setLayout(layout)
        return container
    
    def _create_temp_area(self):
        container = QWidget()
        container.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(Style.config.Layout.BUTTON_SPACING)

        lbl = QLabel("Temperatura (°C):")
        lbl.setFixedWidth(140)
        self.temp_edit = QLineEdit(str(self.program["target_temperature"]))
        self.temp_edit.setPlaceholderText("Ej: 110")

        layout.addWidget(lbl)
        layout.addWidget(self.temp_edit)
        Style.label.apply(lbl,"normal")
        Style.input.apply(self.temp_edit)
        
        container.setLayout(layout)
        return container

    def _create_enabled_area(self):
        container = QWidget()
        container.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(Style.config.Layout.BUTTON_SPACING)

        lbl = QLabel("Habilitado:")
        lbl.setFixedWidth(140)
        self.enabled_check = QCheckBox()
        self.enabled_check.setChecked(self.program["enabled"])


        layout.addWidget(lbl)
        layout.addWidget(self.enabled_check)
        Style.label.apply(lbl,"normal")
        Style.checkbox.apply(self.enabled_check)
        
        container.setLayout(layout)
        return container

    def _create_button_area(self):
        container = QWidget()
        container.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

        layout = QHBoxLayout()
        button_layout_config = Style.layout.buttons()
        layout.setContentsMargins(*button_layout_config["margins"])
        layout.setSpacing(button_layout_config["spacing"])

        self.accept_btn = QPushButton("Aceptar")
        self.cancel_btn = QPushButton("Cancelar")

        self.accept_btn.clicked.connect(self.accept)
        self.cancel_btn.clicked.connect(self.reject)
        
        layout.addWidget(self.accept_btn)
        layout.addWidget(self.cancel_btn)
        Style.button.secondary(self.accept_btn)
        Style.button.secondary(self.cancel_btn)

        container.setLayout(layout)
        return container

    def get_data(self):
        """Validación básica y retorno de datos."""

        # Validar conversión a entero
        try:
            time_val = int(self.time_edit.text().strip())
        except ValueError:
            time_val = None

        try:
            temp_val = int(self.temp_edit.text().strip())
        except ValueError:
            temp_val = None

        return {
            "program_id": self.program["program_id"],
            "program_name": self.name_edit.text(),
            "product_name": self.product_edit.text(),
            "format": self.format_edit.text(),
            "target_time": time_val,
            "target_temperature": temp_val,
            "enabled": self.enabled_check.isChecked(),
        }
