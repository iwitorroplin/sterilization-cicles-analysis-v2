# src/ui/mod_configuracion/general_tab.py

from copy import deepcopy

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
    QCheckBox
)

from src.core.app_settings import AppSettings
from src.style import Style


class GeneralTab(QWidget):

    CONFIG_FILE = "app_config"
    GENERAL_KEY = "general"
    CYCLE_KEY = "cycle_detector"
    
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
        self.current_config = deepcopy(self.default_config)
        self.last_loaded_config = deepcopy(self.default_config)

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



    # ------------------------------------------------------
    # Lógica
    # ------------------------------------------------------

    def initialize(self):
        """Carga la configuración básica en los campos de la pestaña."""
        loaded_config = AppSettings.get_basic_config()
        
        # COnfiguracion GENERAL
        general_config = loaded_config.get(self.GENERAL_KEY, {})
        
        self.current_config = deepcopy(loaded_config)
        self.last_loaded_config = deepcopy(loaded_config)

        printer = general_config.get(
            "printer",
            self.default_config["general"]["printer"]
            )
        ferlo_dir = general_config.get(
            "data_ferlo_dir",
            self.default_config["·general"]["data_ferlo_dir"]
            )
        raw_dir = general_config.get(
            "raw_data_ferlo_dir",
            self.default_config["general"]["raw_data_ferlo_dir"]
            )
        process_dir = general_config.get(
            "process_data_ferlo_dir",
            self.default_config["general"]["process_data_ferlo_dir"]
            )

        index = self.printer_combo.findText(printer)
        self.printer_combo.setCurrentIndex(index if index >= 0 else 0)
        self.ferlo_dir_edit.setText(ferlo_dir)
        self.raw_path_edit.setText(raw_dir)
        self.process_path_edit.setText(process_dir)

        # Configuracion CYCLE DETECTOR
        cycle_config = loaded_config.get(self.CYCLE_KEY, {})
        
        temp_c = cycle_config.get(
            "temperature",
            self.default_config["cycle_detector"]["temperature"]
            )
        auto = cycle_config.get(
            "auto",
            self.default_config["cycle_detector"]["auto"]
            )
        bad_value = cycle_config.get(
            "bad_value",
            self.default_config["cycle_detector"]["bad_value"]
        )
        self.temp_c_edit.setText(temp_c)
        self.auto_cycle_checkbox.setAttribute(auto)
        self.bad_value_edit.setText(bad_value)

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
    
    def _create_ferlo_dir_area(self):
        container = QWidget()
        container.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(Style.config.Layout.BUTTON_SPACING)

        ferlo_dir_lbl = QLabel("Directorio principal:")
        layout.addWidget(ferlo_dir_lbl)

        self.ferlo_dir_edit = QLineEdit()
        self.ferlo_dir_edit.setPlaceholderText("Selecciona el directorio principal...")
        layout.addWidget(self.ferlo_dir_edit)

        browse_btn = QPushButton("...")
        browse_btn.setFixedSize(40, 40)
        browse_btn.clicked.connect(self.browse_raw_path)
        layout.addWidget(browse_btn)

        Style.input.apply(self.ferlo_dir_edit)

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
    
    def _create_start_temperature_c(self):
        container = QWidget()
        container.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        
        layout = QHBoxLayout(container)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(Style.config.Layout.BUTTON_SPACING)

        label = QLabel("Temperatura inicio ciclos:")
        Style.label.apply(label)
        layout.addWidget(label)

        self.temp_c_edit = QLineEdit()
        self.temp_c_edit.setPlaceholderText("Ejemplo: 70")
        Style.input.apply(self.temp_c_edit)
        layout.addWidget(self.temp_c_edit)

        return container

    def _create_auto_cycle_detection(self):
        container = QWidget()
        container.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        
        layout = QHBoxLayout(container)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(Style.config.Layout.BUTTON_SPACING)
        
        label = QLabel("Detección automática de ciclos")
        Style.label.apply(label)
        layout.addWidget(label)

        self.auto_cycle_checkbox = QCheckBox("")
        layout.addWidget(self.auto_cycle_checkbox)
        Style.checkbox.apply(self.auto_cycle_checkbox)

        
        return container
    
    
    def _create_bad_value_area(self):
        container = QWidget()
        container.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(Style.config.Layout.BUTTON_SPACING)

        bad_value_lbl = QLabel("texto de error en los datos:")
        layout.addWidget(bad_value_lbl)

        self.bad_value_edit = QLineEdit()
        self.bad_value_edit.setPlaceholderText("Escribe el error dado en las celdas. Ejemplo: <<<<<<<< ")
        layout.addWidget(self.bad_value_edit)

        Style.input.apply(self.bad_value_edit)

        container.setLayout(layout)
        return container
        
        return
    
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
        # self.restore_btn.clicked.connect(self.restore_defaults)

        self.undo_btn = QPushButton("Deshacer")
        self.undo_btn.setFixedHeight(40)
        self.undo_btn.setMinimumWidth(80)
        # self.undo_btn.clicked.connect(self.undo_changes)

        self.save_btn = QPushButton("Guardar")
        self.save_btn.setFixedHeight(40)
        # self.save_btn.clicked.connect(self.save_config)

        layout.addWidget(self.restore_btn)
        layout.addWidget(self.undo_btn)
        layout.addWidget(self.save_btn)

        Style.button.secondary(self.restore_btn)
        Style.button.secondary(self.undo_btn)
        Style.button.secondary(self.save_btn)

        container.setLayout(layout)
        return container



    def browse_raw_path(self):
        directory = QFileDialog.getExistingDirectory(
            self, "Seleccionar directorio RAW", self.raw_path_edit.text()
        )
        if directory:
            self.raw_path_edit.setText(directory)

    def browse_process_path(self):
        directory = QFileDialog.getExistingDirectory(
            self,
            "Seleccionar directorio de datos procesados",
            self.process_path_edit.text(),
        )
        if directory:
            self.process_path_edit.setText(directory)