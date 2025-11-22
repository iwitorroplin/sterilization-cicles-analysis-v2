from typing import List, Optional
from pathlib import Path
from .dataclasses import ValidationResult
from .constants import MIN_TEMPERATURE, MAX_TEMPERATURE, MIN_TIME, MAX_TIME

class ConfigValidators:
    @staticmethod
    def validate_temperature(temperature: float) -> ValidationResult:
        result = ValidationResult(is_valid=True)
        if not isinstance(temperature, (int, float)):
            result.add_error("La temperatura debe ser un número")
        elif temperature < MIN_TEMPERATURE:
            result.add_error(f"La temperatura no puede ser menor a {MIN_TEMPERATURE}")
        elif temperature > MAX_TEMPERATURE:
            result.add_error(f"La temperatura no puede ser mayor a {MAX_TEMPERATURE}")
        return result
    
    @staticmethod
    def validate_time(time: float) -> ValidationResult:
        result = ValidationResult(is_valid=True)
        if not isinstance(time, (int, float)):
            result.add_error("El tiempo debe ser un número")
        elif time < MIN_TIME:
            result.add_error(f"El tiempo no puede ser menor a {MIN_TIME}")
        elif time > MAX_TIME:
            result.add_error(f"El tiempo no puede ser mayor a {MAX_TIME}")
        return result
    
    @staticmethod
    def validate_directory(path: str) -> ValidationResult:
        result = ValidationResult(is_valid=True)
        if not path.strip():
            result.add_error("La ruta no puede estar vacía")
        # Puedes añadir más validaciones de rutas si es necesario
        return result
    
    @staticmethod
    def validate_text(text: str, field_name: str) -> ValidationResult:
        result = ValidationResult(is_valid=True)
        if not text.strip():
            result.add_error(f"El campo {field_name} no puede estar vacío")
        return result

class ProgramValidators:
    @staticmethod
    def validate_program(program_data: dict) -> ValidationResult:
        result = ValidationResult(is_valid=True)
        
        # Validar nombre del programa
        name_validation = ConfigValidators.validate_text(
            program_data.get('program_name', ''), 'nombre del programa'
        )
        if not name_validation.is_valid:
            result.errors.extend(name_validation.errors)
        
        # Validar producto
        product_validation = ConfigValidators.validate_text(
            program_data.get('product_name', ''), 'producto'
        )
        if not product_validation.is_valid:
            result.errors.extend(product_validation.errors)
        
        # Validar formato
        format_validation = ConfigValidators.validate_text(
            program_data.get('format', ''), 'formato'
        )
        if not format_validation.is_valid:
            result.errors.extend(format_validation.errors)
        
        # Validar temperatura
        temp_validation = ConfigValidators.validate_temperature(
            program_data.get('target_temperature', 0)
        )
        if not temp_validation.is_valid:
            result.errors.extend(temp_validation.errors)
        
        # Validar tiempo
        time_validation = ConfigValidators.validate_time(
            program_data.get('target_time', 0)
        )
        if not time_validation.is_valid:
            result.errors.extend(time_validation.errors)
        
        return result