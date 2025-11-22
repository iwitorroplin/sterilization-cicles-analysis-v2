from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QFormLayout, QLineEdit, 
    QCheckBox, QPushButton, QGroupBox, QMessageBox, QTableWidget,
    QTableWidgetItem, QHeaderView, QLabel, QFileDialog
)
from PySide6.QtCore import Signal, Qt

from ui.widgets.tab_panel import TabPanel
from ui.widgets.validated_input import ValidatedLineEdit, ValidatedDoubleSpinBox
from shared.validators import ConfigValidators
from .models import ProgramFormData

class ConfigView(QWidget):
    config_updated = Signal(str, dict)  # section, config
    program_added = Signal(dict)
    program_updated = Signal(int, dict)
    program_deleted = Signal(int)
    
    def __init__(self):
        super().__init__()
        self.setup_ui()
        self.setup_validators()
    
    def setup_ui(self):
        layout = QVBoxLayout(self)
        
        self.tab_panel = TabPanel()
        
        # Pestañas
        self.general_tab = self.create_general_tab()
        self.tab_panel.add_tab("General", self.general_tab)
        
        self.cycle_detector_tab = self.create_cycle_detector_tab()
        self.tab_panel.add_tab("Cycle Detector", self.cycle_detector_tab)
        
        self.programs_tab = self.create_programs_tab()
        self.tab_panel.add_tab("Programas", self.programs_tab)
        
        layout.addWidget(self.tab_panel)
    
    def setup_validators(self):
        # Validadores para rutas
        self.data_ferlo_dir_input.set_validator(
            lambda x: ConfigValidators.validate_directory(x).is_valid
        )
        self.raw_data_dir_input.set_validator(
            lambda x: ConfigValidators.validate_directory(x).is_valid
        )
        self.process_data_dir_input.set_validator(
            lambda x: ConfigValidators.validate_directory(x).is_valid
        )
    
    def create_general_tab(self) -> QWidget:
        tab = QWidget()
        layout = QVBoxLayout(tab)
        
        # Grupo de configuración general
        general_group = QGroupBox("Configuración General")
        general_layout = QFormLayout(general_group)
        
        self.printer_input = QLineEdit()
        self.data_ferlo_dir_input = ValidatedLineEdit()
        self.raw_data_dir_input = ValidatedLineEdit()
        self.process_data_dir_input = ValidatedLineEdit()
        
        # Botones para seleccionar directorios
        dir_buttons_layout = QHBoxLayout()
        self.select_data_dir_btn = QPushButton("Seleccionar")
        self.select_raw_dir_btn = QPushButton("Seleccionar")
        self.select_process_dir_btn = QPushButton("Seleccionar")
        
        dir_buttons_layout.addWidget(self.select_data_dir_btn)
        dir_buttons_layout.addWidget(self.select_raw_dir_btn)
        dir_buttons_layout.addWidget(self.select_process_dir_btn)
        
        general_layout.addRow("Impresora:", self.printer_input)
        general_layout.addRow("Directorio Ferlo:", self.data_ferlo_dir_input)
        general_layout.addRow("Directorio Raw:", self.raw_data_dir_input)
        general_layout.addRow("Directorio Process:", self.process_data_dir_input)
        general_layout.addRow("", dir_buttons_layout)
        
        # Botón de guardar
        self.save_general_btn = QPushButton("Guardar Configuración General")
        self.save_general_btn.clicked.connect(self.save_general_config)
        
        layout.addWidget(general_group)
        layout.addWidget(self.save_general_btn)
        layout.addStretch()
        
        return tab
    
    def create_cycle_detector_tab(self) -> QWidget:
        tab = QWidget()
        layout = QVBoxLayout(tab)
        
        cycle_group = QGroupBox("Configuración del Detector de Ciclos")
        cycle_layout = QFormLayout(cycle_group)
        
        self.temperature_input = ValidatedDoubleSpinBox(0, 300)
        self.temperature_input.setValue(70.0)
        self.auto_checkbox = QCheckBox()
        self.auto_checkbox.setChecked(True)
        self.bad_value_input = QLineEdit()
        self.bad_value_input.setText("<<<<<<<<")
        
        cycle_layout.addRow("Temperatura:", self.temperature_input)
        cycle_layout.addRow("Auto:", self.auto_checkbox)
        cycle_layout.addRow("Bad Value:", self.bad_value_input)
        
        self.save_cycle_btn = QPushButton("Guardar Cycle Detector")
        self.save_cycle_btn.clicked.connect(self.save_cycle_detector_config)
        
        layout.addWidget(cycle_group)
        layout.addWidget(self.save_cycle_btn)
        layout.addStretch()
        
        return tab
    
    def create_programs_tab(self) -> QWidget:
        tab = QWidget()
        layout = QVBoxLayout(tab)
        
        # Tabla de programas
        self.programs_table = QTableWidget()
        self.programs_table.setColumnCount(7)
        self.programs_table.setHorizontalHeaderLabels([
            "ID", "Nombre", "Producto", "Formato", "Tiempo", "Temp.", "Habilitado"
        ])
        self.programs_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        
        # Botones de acción
        btn_layout = QHBoxLayout()
        self.add_program_btn = QPushButton("Añadir Programa")
        self.edit_program_btn = QPushButton("Editar Programa")
        self.delete_program_btn = QPushButton("Eliminar Programa")
        
        btn_layout.addWidget(self.add_program_btn)
        btn_layout.addWidget(self.edit_program_btn)
        btn_layout.addWidget(self.delete_program_btn)
        
        # Formulario de programa
        self.program_form = self.create_program_form()
        self.program_form.hide()
        
        layout.addWidget(self.programs_table)
        layout.addLayout(btn_layout)
        layout.addWidget(self.program_form)
        
        # Conectar señales
        self.add_program_btn.clicked.connect(self.show_add_program_form)
        self.edit_program_btn.clicked.connect(self.show_edit_program_form)
        self.delete_program_btn.clicked.connect(self.delete_program)
        
        return tab
    
    def create_program_form(self) -> QGroupBox:
        form = QGroupBox("Formulario de Programa")
        layout = QFormLayout(form)
        
        self.program_id_input = QLineEdit()
        self.program_id_input.setEnabled(False)
        
        self.program_name_input = ValidatedLineEdit(
            validator=lambda x: ConfigValidators.validate_text(x, "nombre").is_valid
        )
        self.product_name_input = ValidatedLineEdit(
            validator=lambda x: ConfigValidators.validate_text(x, "producto").is_valid
        )
        self.format_input = ValidatedLineEdit(
            validator=lambda x: ConfigValidators.validate_text(x, "formato").is_valid
        )
        
        self.target_time_input = ValidatedDoubleSpinBox(0, 1000)
        self.target_time_input.setValue(50.0)
        
        self.target_temp_input = ValidatedDoubleSpinBox(0, 300)
        self.target_temp_input.setValue(110.0)
        
        self.enabled_checkbox = QCheckBox()
        self.enabled_checkbox.setChecked(True)
        
        # Botones del formulario
        btn_layout = QHBoxLayout()
        self.save_program_btn = QPushButton("Guardar")
        self.cancel_program_btn = QPushButton("Cancelar")
        
        btn_layout.addWidget(self.save_program_btn)
        btn_layout.addWidget(self.cancel_program_btn)
        
        layout.addRow("ID:", self.program_id_input)
        layout.addRow("Nombre Programa:", self.program_name_input)
        layout.addRow("Producto:", self.product_name_input)
        layout.addRow("Formato:", self.format_input)
        layout.addRow("Tiempo Objetivo:", self.target_time_input)
        layout.addRow("Temp. Objetivo:", self.target_temp_input)
        layout.addRow("Habilitado:", self.enabled_checkbox)
        layout.addRow(btn_layout)
        
        # Conectar señales
        self.save_program_btn.clicked.connect(self.save_program)
        self.cancel_program_btn.clicked.connect(self.hide_program_form)
        
        return form
    
    def save_general_config(self):
        """Guarda la configuración general"""
        config = {
            "printer": self.printer_input.text(),
            "data_ferlo_dir": self.data_ferlo_dir_input.text(),
            "raw_data_ferlo_dir": self.raw_data_dir_input.text(),
            "process_data_ferlo_dir": self.process_data_dir_input.text()
        }
        self.config_updated.emit("general", config)
        QMessageBox.information(self, "Éxito", "Configuración general guardada")
    
    def save_cycle_detector_config(self):
        """Guarda la configuración del cycle detector"""
        config = {
            "temperature": self.temperature_input.value(),
            "auto": self.auto_checkbox.isChecked(),
            "bad_value": self.bad_value_input.text()
        }
        self.config_updated.emit("cycle_detector", config)
        QMessageBox.information(self, "Éxito", "Configuración del detector guardada")
    
    def show_add_program_form(self):
        """Muestra el formulario para añadir programa"""
        form_data = ProgramFormData()
        self.load_program_form(form_data)
        self.program_form.show()
    
    def show_edit_program_form(self):
        """Muestra el formulario para editar programa"""
        selected = self.programs_table.currentRow()
        if selected < 0:
            QMessageBox.warning(self, "Error", "Selecciona un programa para editar")
            return
        
        program_id = int(self.programs_table.item(selected, 0).text())
        self.edit_program_btn.setProperty("editing_id", program_id)
        
        # Solicitar datos del programa al controlador
        self.edit_program_btn.clicked.emit()
    
    def load_program_form(self, program_data: ProgramFormData):
        """Carga los datos en el formulario de programa"""
        self.program_id_input.setText(str(program_data.program_id))
        self.program_name_input.setText(program_data.program_name)
        self.product_name_input.setText(program_data.product_name)
        self.format_input.setText(program_data.format)
        self.target_time_input.setValue(program_data.target_time)
        self.target_temp_input.setValue(program_data.target_temperature)
        self.enabled_checkbox.setChecked(program_data.enabled)
    
    def get_program_form_data(self) -> ProgramFormData:
        """Obtiene los datos del formulario de programa"""
        return ProgramFormData(
            program_id=int(self.program_id_input.text()) if self.program_id_input.text() else 0,
            program_name=self.program_name_input.text(),
            product_name=self.product_name_input.text(),
            format=self.format_input.text(),
            target_time=self.target_time_input.value(),
            target_temperature=self.target_temp_input.value(),
            enabled=self.enabled_checkbox.isChecked()
        )
    
    def save_program(self):
        """Guarda el programa desde el formulario"""
        program_data = self.get_program_form_data()
        
        if program_data.program_id > 0:
            # Actualizar programa existente
            self.program_updated.emit(program_data.program_id, program_data.to_dict())
        else:
            # Añadir nuevo programa
            self.program_added.emit(program_data.to_dict())
        
        self.hide_program_form()
    
    def hide_program_form(self):
        self.program_form.hide()
    
    def delete_program(self):
        """Elimina el programa seleccionado"""
        selected = self.programs_table.currentRow()
        if selected < 0:
            QMessageBox.warning(self, "Error", "Selecciona un programa para eliminar")
            return
        
        program_id = int(self.programs_table.item(selected, 0).text())
        program_name = self.programs_table.item(selected, 1).text()
        
        reply = QMessageBox.question(
            self, "Confirmar Eliminación",
            f"¿Estás seguro de que quieres eliminar el programa '{program_name}'?",
            QMessageBox.Yes | QMessageBox.No
        )
        
        if reply == QMessageBox.Yes:
            self.program_deleted.emit(program_id)
    
    def load_app_config(self, config):
        """Carga la configuración de la aplicación en la vista"""
        # Configuración general
        self.printer_input.setText(config.general.printer)
        self.data_ferlo_dir_input.setText(config.general.data_ferlo_dir)
        self.raw_data_dir_input.setText(config.general.raw_data_ferlo_dir)
        self.process_data_dir_input.setText(config.general.process_data_ferlo_dir)
        
        # Cycle detector
        self.temperature_input.setValue(config.cycle_detector.temperature)
        self.auto_checkbox.setChecked(config.cycle_detector.auto)
        self.bad_value_input.setText(config.cycle_detector.bad_value)
    
    def load_programs_config(self, programs):
        """Carga la configuración de programas en la tabla"""
        self.programs_table.setRowCount(len(programs))
        
        for row, program in enumerate(programs):
            self.programs_table.setItem(row, 0, QTableWidgetItem(str(program.program_id)))
            self.programs_table.setItem(row, 1, QTableWidgetItem(program.program_name))
            self.programs_table.setItem(row, 2, QTableWidgetItem(program.product_name))
            self.programs_table.setItem(row, 3, QTableWidgetItem(program.format))
            self.programs_table.setItem(row, 4, QTableWidgetItem(str(program.target_time)))
            self.programs_table.setItem(row, 5, QTableWidgetItem(str(program.target_temperature)))
            
            enabled_item = QTableWidgetItem("Sí" if program.enabled else "No")
            enabled_item.setTextAlignment(Qt.AlignCenter)
            self.programs_table.setItem(row, 6, enabled_item)