# src/ui/mod_configuracion/general_tab.py

from PySide6.QtWidgets import (
    QFileDialog,
    QLabel,
    QComboBox,
    QHBoxLayout,
    QLineEdit,
    QMessageBox,
    QPushButton,
    QSizePolicy,
    QVBoxLayout,
    QWidget,
)

from src.style import Style


class GeneralTab(QWidget):

    CONFIG_FILE = "app_config"
    CONFIG_KEY = "general"

    def __init__(self):
        QWidget.__init__(self)

        # Valores por defecto
        self.default_config = {  
            "general": {
                "printer": "Predeterminada",
                "data_ferlo_dir": "C:/Users/Usuario/Desktop/ferlo",
                "raw_data_ferlo_dir": "C:/Users/Usuario/Desktop/ferlo/raw",
                "process_data_ferlo_dir": "C:/Users/Usuario/Desktop/ferlo/process"
            },
            "cycle_detector": {
                "temperature_cycle_detector": 70,
                "auto_cycle_detection": True,
                "bad_value_cycle_detector": "<<<<<<<<"
            }
        }


        # Copias internas
        self.current_config = self.default_config.copy()
        self.last_loaded_config = self.default_config.copy()

        self._setup_ui()
        self.initialize()

    # ------------------------------------------------------
    # UI
    # ------------------------------------------------------

    def _setup_ui(self):
        layout = QVBoxLayout()
        main_layout_config = Style.layout.main()
        layout.setContentsMargins(*main_layout_config["margins"])
        layout.setSpacing(main_layout_config["spacing"])

        work_area_layout = QVBoxLayout()
        work_area_layout.setContentsMargins(0, 0, 0, 0)
        work_area_layout.setSpacing(Style.config.Layout.MAIN_SPACING)

        work_area_layout.addWidget(self._create_printer_area())
        work_area_layout.addWidget(self._create_raw_data_area())
        work_area_layout.addWidget(self._create_process_data_area())
        work_area_layout.addStretch()
        work_area_layout.addWidget(self._create_button_area())

        layout.addLayout(work_area_layout)
        self.setLayout(layout)
        Style.widget.apply(self)

    def _create_printer_area(self):
        """Crea el área de selección de impresora"""
        container = QWidget()
        container.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(Style.config.Layout.BUTTON_SPACING)

        lbl_printer = QLabel("Impresora:")
        layout.addWidget(lbl_printer)

        self.printer_combo = QComboBox()
        self.printer_combo.addItems(["Predeterminada", "Impresora 1", "Impresora 2"])
        layout.addWidget(self.printer_combo)

        Style.label.apply(lbl_printer, "normal")
        Style.combobox.apply(self.printer_combo)

        container.setLayout(layout)
        return container

    def _create_raw_data_area(self):
        container = QWidget()
        container.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(Style.config.Layout.BUTTON_SPACING)

        lbl_raw = QLabel("Directorio RAW:")
        layout.addWidget(lbl_raw)

        self.raw_path_edit = QLineEdit()
        self.raw_path_edit.setPlaceholderText("Selecciona el directorio de datos RAW...")
        layout.addWidget(self.raw_path_edit)

        browse_btn = QPushButton("...")
        browse_btn.setFixedSize(40, 40)
        browse_btn.clicked.connect(self.browse_raw_path)
        layout.addWidget(browse_btn)

        Style.input.apply(self.raw_path_edit)

        container.setLayout(layout)
        return container

    def _create_process_data_area(self):
        container = QWidget()
        container.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(Style.config.Layout.BUTTON_SPACING)

        lbl_process = QLabel("Directorio Process:")
        lbl_process.setFixedWidth(130)
        layout.addWidget(lbl_process)

        self.process_path_edit = QLineEdit()
        self.process_path_edit.setPlaceholderText(
            "Selecciona el directorio donde guardar procesados..."
        )
        layout.addWidget(self.process_path_edit)

        browse_btn = QPushButton("...")
        browse_btn.setFixedSize(40, 40)
        browse_btn.clicked.connect(self.browse_process_path)
        layout.addWidget(browse_btn)

        Style.input.apply(self.process_path_edit)

        container.setLayout(layout)
        return container

    def _create_button_area(self):
        container = QWidget()
        container.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

        layout = QHBoxLayout()
        button_layout_config = Style.layout.buttons()
        layout.setContentsMargins(*button_layout_config["margins"])
        layout.setSpacing(button_layout_config["spacing"])

        self.restore_btn = QPushButton("Restaurar")
        self.restore_btn.setFixedHeight(40)
        self.restore_btn.setMinimumWidth(80)
        self.restore_btn.clicked.connect(self.restore_defaults)

        self.undo_btn = QPushButton("Deshacer")
        self.undo_btn.setFixedHeight(40)
        self.undo_btn.setMinimumWidth(80)
        self.undo_btn.clicked.connect(self.undo_changes)

        self.save_btn = QPushButton("Guardar")
        self.save_btn.setFixedHeight(40)
        self.save_btn.clicked.connect(self.save_config)

        layout.addWidget(self.restore_btn)
        layout.addWidget(self.undo_btn)
        layout.addWidget(self.save_btn)

        Style.button.secondary(self.restore_btn)
        Style.button.secondary(self.undo_btn)
        Style.button.secondary(self.save_btn)

        container.setLayout(layout)
        return container

