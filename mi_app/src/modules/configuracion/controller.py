from modules.base_module import BaseModule
from .view import ConfigView
from .models import ProgramFormData
from core.session import Session
from shared.validators import ProgramValidators
from shared.dataclasses import ValidationResult

class ConfigController(BaseModule):
    def __init__(self):
        super().__init__("Configuración")
        self._view = ConfigView()
        self._session = Session()
        
        # Conectar señales
        self._view.config_updated.connect(self.update_app_config)
        self._view.program_added.connect(self.add_program)
        self._view.program_updated.connect(self.update_program)
        self._view.program_deleted.connect(self.delete_program)
        
        # Conectar botones de edición
        self._view.edit_program_btn.clicked.connect(self.load_program_for_editing)
        
        # Cargar configuraciones
        self.load_configurations()
    
    def get_view(self):
        return self._view
    
    def get_controller(self):
        return self
    
    def load_configurations(self):
        """Carga todas las configuraciones en la vista"""
        config_service = self._session.get_config_service()
        
        # Cargar configuración de la aplicación
        app_config = config_service.get_app_config()
        self._view.load_app_config(app_config)
        
        # Cargar configuración de programas
        programs_config = config_service.get_programs_config()
        self._view.load_programs_config(programs_config.programs)
    
    def update_app_config(self, section: str, config: dict):
        """Actualiza la configuración de la aplicación"""
        config_service = self._session.get_config_service()
        config_service.update_app_config(section, config)
    
    def add_program(self, program_data: dict):
        """Añade un nuevo programa"""
        # Validar datos del programa
        validation = ProgramValidators.validate_program(program_data)
        if not validation.is_valid:
            self._show_validation_errors(validation.errors)
            return
        
        config_service = self._session.get_config_service()
        program_id = config_service.add_program(program_data)
        
        # Recargar vista
        programs_config = config_service.get_programs_config()
        self._view.load_programs_config(programs_config.programs)
    
    def update_program(self, program_id: int, program_data: dict):
        """Actualiza un programa existente"""
        # Validar datos del programa
        validation = ProgramValidators.validate_program(program_data)
        if not validation.is_valid:
            self._show_validation_errors(validation.errors)
            return
        
        config_service = self._session.get_config_service()
        config_service.update_program(program_id, program_data)
        
        # Recargar vista
        programs_config = config_service.get_programs_config()
        self._view.load_programs_config(programs_config.programs)
    
    def delete_program(self, program_id: int):
        """Elimina un programa"""
        config_service = self._session.get_config_service()
        config_service.delete_program(program_id)
        
        # Recargar vista
        programs_config = config_service.get_programs_config()
        self._view.load_programs_config(programs_config.programs)
    
    def load_program_for_editing(self):
        """Carga un programa para edición"""
        program_id = self._view.edit_program_btn.property("editing_id")
        if program_id:
            config_service = self._session.get_config_service()
            program = config_service.get_program(program_id)
            
            if program:
                form_data = ProgramFormData(
                    program_id=program.program_id,
                    program_name=program.program_name,
                    product_name=program.product_name,
                    format=program.format,
                    target_time=program.target_time,
                    target_temperature=program.target_temperature,
                    enabled=program.enabled
                )
                self._view.load_program_form(form_data)
                self._view.program_form.show()
    
    def _show_validation_errors(self, errors: list):
        """Muestra errores de validación"""
        error_text = "Errores de validación:\n• " + "\n• ".join(errors)
        from PySide6.QtWidgets import QMessageBox
        QMessageBox.warning(self._view, "Error de Validación", error_text)
    
    def on_activate(self):
        """Se ejecuta cuando el módulo se activa"""
        self.load_configurations()