from __future__ import annotations

from pathlib import Path
from typing import Dict

from .constants import MAX_TEMPERATURE, MIN_TEMPERATURE, MAX_TIME, MIN_TIME
from .dataclasses import ValidationResult


class ConfigValidators:
    @staticmethod
    def validate_temperature(temperature: float) -> ValidationResult:
        result = ValidationResult(is_valid=True)
        if not isinstance(temperature, (int, float)):
            result.add_error("La temperatura debe ser numérica")
        elif temperature < MIN_TEMPERATURE:
            result.add_error(f"La temperatura debe ser mayor a {MIN_TEMPERATURE}")
        elif temperature > MAX_TEMPERATURE:
            result.add_error(f"La temperatura debe ser menor a {MAX_TEMPERATURE}")
        return result

    @staticmethod
    def validate_time(seconds: float) -> ValidationResult:
        result = ValidationResult(is_valid=True)
        if not isinstance(seconds, (int, float)):
            result.add_error("El tiempo debe ser numérico")
        elif seconds < MIN_TIME:
            result.add_error(f"El tiempo debe ser mayor a {MIN_TIME}")
        elif seconds > MAX_TIME:
            result.add_error(f"El tiempo debe ser menor a {MAX_TIME}")
        return result

    @staticmethod
    def validate_directory(path: str) -> ValidationResult:
        result = ValidationResult(is_valid=True)
        if not path.strip():
            result.add_error("La ruta no puede estar vacía")
        return result

    @staticmethod
    def validate_text(text: str, field_name: str) -> ValidationResult:
        result = ValidationResult(is_valid=True)
        if not text.strip():
            result.add_error(f"El campo {field_name} no puede estar vacío")
        return result


class ProgramValidators:
    @staticmethod
    def validate_program(program_data: Dict[str, object]) -> ValidationResult:
        result = ValidationResult(is_valid=True)

        for field, label in [
            ("program_name", "nombre del programa"),
            ("product_name", "producto"),
            ("format", "formato"),
        ]:
            text_validation = ConfigValidators.validate_text(str(program_data.get(field, "")), label)
            if not text_validation.is_valid:
                result.errors.extend(text_validation.errors)

        temperature_validation = ConfigValidators.validate_temperature(float(program_data.get("target_temperature", 0)))
        if not temperature_validation.is_valid:
            result.errors.extend(temperature_validation.errors)

        time_validation = ConfigValidators.validate_time(float(program_data.get("target_time", 0)))
        if not time_validation.is_valid:
            result.errors.extend(time_validation.errors)

        if result.errors:
            result.is_valid = False
        return result
