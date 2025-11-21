# programas_tab.py
import copy

from PySide6.QtWidgets import (
    QAbstractItemView,
    QDialog,
    QHeaderView,
    QHBoxLayout,
    QLabel,
    QMessageBox,
    QPushButton,
    QSizePolicy,
    QTableWidget,
    QTableWidgetItem,
    QVBoxLayout,
    QWidget,
)

from src.ui.widgets.programs_dialog import ProgramDialog

# from src.core.app_settings import AppSettings
from src.style import Style


class ProgramsTab(QWidget):
    PROGRAMS_FILE = "ferlo_programs"
    PROGRAMS_KEY  = "programs"
    
    def __init__(self):
        super().__init__()

        # Valores por defecto para programas
        self.default_config = {
            "programs": [
                {
                    "program_id": 99,
                    "program_name": "Nuevo Programa",
                    "product_name": "Undefined",
                    "format": "Undefined",
                    "target_time": 1,
                    "target_temperature": 110,
                    "enabled": False
                },

            ]
        }

        # Copias internas
        self.current_config = copy.deepcopy(self.default_config)
        self.last_loaded_config = copy.deepcopy(self.default_config)

        self._setup_ui()
        # self._initialize()
    
    def _setup_ui(self):
        layout = QVBoxLayout()
        main_layout_config = Style.layout.main()
        layout.setContentsMargins(*main_layout_config["margins"])
        layout.setSpacing(main_layout_config["spacing"]) 

        work_area_layout = QVBoxLayout()
        work_area_layout.setContentsMargins(0, 0, 0, 0)
        work_area_layout.setSpacing(Style.config.Layout.MAIN_SPACING)

        # work_area_layout.addWidget()
        work_area_layout.addStretch()
        work_area_layout.addWidget(self._create_button_area())

        layout.addLayout(work_area_layout)
        self.setLayout(layout)
        Style.widget.apply(self)


    def _create_button_area(self):
        container = QWidget()
        container.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

        layout = QHBoxLayout()
        button_layout_config = Style.layout.buttons()
        layout.setContentsMargins(*button_layout_config["margins"])
        layout.setSpacing(button_layout_config["spacing"])

        self.add_btn = QPushButton("Añadir")
        self.add_btn.clicked.connect(self.add_new_program)

        self.edit_btn = QPushButton("Modificar")
        # self.edit_btn.clicked.connect(self.edit_selected_program)

        self.delete_btn = QPushButton("Eliminar")
        # self.delete_btn.clicked.connect(self.delete_selected_program)

        self.restore_btn = QPushButton("Restaurar")
        # self.restore_btn.clicked.connect(self.restore_defaults)

        self.undo_btn = QPushButton("Deshacer")
        # self.undo_btn.clicked.connect(self.undo_changes)

        self.save_btn = QPushButton("Guardar")
        # self.save_btn.clicked.connect(self.save_config)


        layout.addWidget(self.add_btn)
        layout.addWidget(self.edit_btn)
        layout.addWidget(self.delete_btn)
        layout.addWidget(self.restore_btn)
        layout.addWidget(self.undo_btn)
        layout.addWidget(self.save_btn)
        
        Style.button.secondary(self.add_btn)
        Style.button.secondary(self.edit_btn)
        Style.button.secondary(self.delete_btn)
        Style.button.secondary(self.restore_btn)
        Style.button.secondary(self.undo_btn)
        Style.button.secondary(self.save_btn)
        
        # Estado inicial: sin selección en la tabla
        self.edit_btn.setEnabled(False)
        self.delete_btn.setEnabled(False)
        
        container.setLayout(layout)
        return container

    # ------------------------------------------------------
    # Gestión de Programas
    # ------------------------------------------------------
    def add_new_program(self):
        dialog = ProgramDialog(self)

        if dialog.exec() == QDialog.Accepted:
            new_program = dialog.get_data()
            # Asignar nuevo ID
            new_program["program_id"] = self.next_program_id
            self.next_program_id += 1

            self.current_config["programs"].append(new_program)
            # self.refresh_table()
            # self.select_program_in_table(new_program["program_id"])
