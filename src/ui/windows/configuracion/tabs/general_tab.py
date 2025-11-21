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


from src.style import Style
from src.ui.windows.configuracion.logic import 


class GeneralTab(QWidget):
   
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
        self._initialize()


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
        work_area_layout.addWidget(self._create_ferlo_dir_area())
        work_area_layout.addWidget(self._create_raw_data_area())
        work_area_layout.addWidget(self._create_process_data_area())
        work_area_layout.addWidget(self._create_start_temperature_c())
        work_area_layout.addWidget(self._create_bad_value_area())
        work_area_layout.addWidget(self._create_auto_cycle_detection())
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
        
        self.printer_combo = QComboBox()
        self.printer_combo.addItems(["Predeterminada", "Impresora 1", "Impresora 2"])
        
        layout.addWidget(lbl_printer)
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

        self.ferlo_dir_edit = QLineEdit()
        self.ferlo_dir_edit.setPlaceholderText("Selecciona el directorio principal...")

        browse_btn = QPushButton("...")
        browse_btn.clicked.connect(self.browse_ferlo_dir)

        layout.addWidget(ferlo_dir_lbl)
        layout.addWidget(self.ferlo_dir_edit)
        layout.addWidget(browse_btn)
        
        Style.label.apply(ferlo_dir_lbl)
        Style.input.apply(self.ferlo_dir_edit)
        Style.button.terciary(browse_btn)

        container.setLayout(layout)
        return container

    def _create_raw_data_area(self):
        container = QWidget()
        container.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(Style.config.Layout.BUTTON_SPACING)

        raw_lbl = QLabel("Directorio RAW:")
        
        self.raw_path_edit = QLineEdit()
        self.raw_path_edit.setPlaceholderText(
            "Selecciona el directorio de datos RAW..."
            )

        browse_btn = QPushButton("...")
        browse_btn.clicked.connect(self.browse_raw_path)

        layout.addWidget(raw_lbl)
        layout.addWidget(self.raw_path_edit)
        layout.addWidget(browse_btn)

        Style.label.apply(raw_lbl)
        Style.input.apply(self.raw_path_edit)
        Style.button.terciary(browse_btn)

        container.setLayout(layout)
        return container

    def _create_process_data_area(self):
        container = QWidget()
        container.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(Style.config.Layout.BUTTON_SPACING)

        process_lbl = QLabel("Directorio Process:")
        
        self.process_path_edit = QLineEdit()
        self.process_path_edit.setPlaceholderText(
            "Selecciona el directorio donde guardar procesados..."
            )
       
        browse_btn = QPushButton("...")
        browse_btn.clicked.connect(self.browse_process_path)

        layout.addWidget(process_lbl)
        layout.addWidget(self.process_path_edit)
        layout.addWidget(browse_btn)
        
        Style.label.apply(process_lbl)
        Style.input.apply(self.process_path_edit)
        Style.button.terciary(browse_btn)
        
        container.setLayout(layout)
        return container
    
    def _create_start_temperature_c(self):
        container = QWidget()
        container.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        
        layout = QHBoxLayout(container)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(Style.config.Layout.BUTTON_SPACING)

        temp_c_label = QLabel("Temperatura inicio ciclos:")
        
        self.temp_c_edit = QLineEdit()
        self.temp_c_edit.setPlaceholderText("Ejemplo: 70")
        
        layout.addWidget(temp_c_label)
        layout.addWidget(self.temp_c_edit)
        
        Style.label.apply(temp_c_label)
        Style.input.apply(self.temp_c_edit)
        
        container.setLayout(layout)
        return container

    def _create_auto_cycle_detection(self):
        container = QWidget()
        container.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        
        layout = QHBoxLayout(container)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(Style.config.Layout.BUTTON_SPACING)
        
        label = QLabel("Detección automática de ciclos")
        
        self.auto_cycle_checkbox = QCheckBox("")
        
        layout.addWidget(label)
        layout.addWidget(self.auto_cycle_checkbox)
        
        Style.label.apply(label)
        Style.checkbox.apply(self.auto_cycle_checkbox)
        
        return container    
    
    def _create_bad_value_area(self):
        container = QWidget()
        container.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(Style.config.Layout.BUTTON_SPACING)

        bad_value_lbl = QLabel("texto de error en los datos:")

        self.bad_value_edit = QLineEdit()
        self.bad_value_edit.setPlaceholderText(
            "Escribe el error dado en las celdas. Ejemplo: <<<<<<<< ")
        
        layout.addWidget(bad_value_lbl)
        layout.addWidget(self.bad_value_edit)

        Style.label.apply(bad_value_lbl)
        Style.input.apply(self.bad_value_edit)

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
        # self.restore_btn.clicked.connect(self.restore_defaults)

        self.undo_btn = QPushButton("Deshacer")
        # self.undo_btn.clicked.connect(self.undo_changes)

        self.save_btn = QPushButton("Guardar")
        # self.save_btn.clicked.connect(self.save_config)

        layout.addWidget(self.restore_btn)
        layout.addWidget(self.undo_btn)
        layout.addWidget(self.save_btn)

        Style.button.secondary(self.restore_btn)
        Style.button.secondary(self.undo_btn)
        Style.button.secondary(self.save_btn)

        container.setLayout(layout)
        return container

