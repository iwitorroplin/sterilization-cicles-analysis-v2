import json
import shutil
from datetime import datetime
from pathlib import Path
from typing import Dict, Any, List, Optional

from ..constants import *
from ..dataclasses import AppConfig, GeneralConfig, CycleDetectorConfig, ProgramsConfig, ProgramConfig

class ConfigService:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ConfigService, cls).__new__(cls)
            cls._instance._initialized = False
        return cls._instance
    
    def __init__(self):
        if self._initialized:
            return
            
        # Crear directorios necesarios
        CONFIG_DIR.mkdir(exist_ok=True)
        BACKUP_DIR.mkdir(exist_ok=True)
        
        # Cargar configuraciones
        self.app_config = self._load_app_config()
        self.programs_config = self._load_programs_config()
        
        self._initialized = True
    
    def _create_backup(self, file_path: Path):
        """Crea un backup del archivo de configuración"""
        if file_path.exists():
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            backup_name = f"{file_path.stem}_{timestamp}{file_path.suffix}"
            backup_path = BACKUP_DIR / backup_name
            shutil.copy2(file_path, backup_path)
            
            # Limitar a 5 backups por archivo
            self._cleanup_old_backups(file_path.stem)
    
    def _cleanup_old_backups(self, config_name: str):
        """Mantiene solo los 5 backups más recientes"""
        backups = sorted(BACKUP_DIR.glob(f"{config_name}_*"))
        if len(backups) > 5:
            for old_backup in backups[:-5]:
                old_backup.unlink()
    
    def _load_app_config(self) -> AppConfig:
        """Carga la configuración de la aplicación"""
        if not APP_CONFIG_FILE.exists():
            default_config = AppConfig(
                general=GeneralConfig(**DEFAULT_APP_CONFIG["general"]),
                cycle_detector=CycleDetectorConfig(**DEFAULT_APP_CONFIG["cycle_detector"])
            )
            self._save_app_config(default_config)
            return default_config
        
        try:
            with open(APP_CONFIG_FILE, 'r', encoding='utf-8') as f:
                data = json.load(f)
                
            return AppConfig(
                general=GeneralConfig(**data.get("general", DEFAULT_APP_CONFIG["general"])),
                cycle_detector=CycleDetectorConfig(**data.get("cycle_detector", DEFAULT_APP_CONFIG["cycle_detector"]))
            )
        except Exception as e:
            print(f"Error cargando app_config: {e}")
            # Crear configuración por defecto en caso de error
            return AppConfig(
                general=GeneralConfig(**DEFAULT_APP_CONFIG["general"]),
                cycle_detector=CycleDetectorConfig(**DEFAULT_APP_CONFIG["cycle_detector"])
            )
    
    def _load_programs_config(self) -> ProgramsConfig:
        """Carga la configuración de programas"""
        if not PROGRAMS_CONFIG_FILE.exists():
            default_programs = [
                ProgramConfig(**program_data) 
                for program_data in DEFAULT_PROGRAMS_CONFIG["programs"]
            ]
            default_config = ProgramsConfig(programs=default_programs)
            self._save_programs_config(default_config)
            return default_config
        
        try:
            with open(PROGRAMS_CONFIG_FILE, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            programs = [
                ProgramConfig(**program_data) 
                for program_data in data.get("programs", [])
            ]
            return ProgramsConfig(programs=programs)
            
        except Exception as e:
            print(f"Error cargando programs_config: {e}")
            default_programs = [
                ProgramConfig(**program_data) 
                for program_data in DEFAULT_PROGRAMS_CONFIG["programs"]
            ]
            return ProgramsConfig(programs=default_programs)
    
    def _save_app_config(self, config: AppConfig):
        """Guarda la configuración de la aplicación"""
        try:
            self._create_backup(APP_CONFIG_FILE)
            with open(APP_CONFIG_FILE, 'w', encoding='utf-8') as f:
                json.dump(config.to_dict(), f, indent=2, ensure_ascii=False)
        except Exception as e:
            print(f"Error guardando app_config: {e}")
    
    def _save_programs_config(self, config: ProgramsConfig):
        """Guarda la configuración de programas"""
        try:
            self._create_backup(PROGRAMS_CONFIG_FILE)
            with open(PROGRAMS_CONFIG_FILE, 'w', encoding='utf-8') as f:
                json.dump(config.to_dict(), f, indent=2, ensure_ascii=False)
        except Exception as e:
            print(f"Error guardando programs_config: {e}")
    
    # Métodos públicos
    def get_app_config(self) -> AppConfig:
        return self.app_config
    
    def update_app_config(self, section: str, config_data: Dict[str, Any]):
        """Actualiza una sección de la configuración"""
        if section == "general":
            self.app_config.general = GeneralConfig(**config_data)
        elif section == "cycle_detector":
            self.app_config.cycle_detector = CycleDetectorConfig(**config_data)
        else:
            raise ValueError(f"Sección desconocida: {section}")
        
        self._save_app_config(self.app_config)
    
    def get_programs_config(self) -> ProgramsConfig:
        return self.programs_config
    
    def update_programs_config(self, config: ProgramsConfig):
        """Actualiza la configuración completa de programas"""
        self.programs_config = config
        self._save_programs_config(config)
    
    def get_program(self, program_id: int) -> Optional[ProgramConfig]:
        for program in self.programs_config.programs:
            if program.program_id == program_id:
                return program
        return None
    
    def add_program(self, program_data: Dict[str, Any]) -> int:
        """Añade un nuevo programa y retorna el ID asignado"""
        programs = self.programs_config.programs
        
        # Generar nuevo ID
        max_id = max([p.program_id for p in programs]) if programs else 0
        new_id = max_id + 1
        
        program_data["program_id"] = new_id
        new_program = ProgramConfig(**program_data)
        
        programs.append(new_program)
        self.programs_config.programs = programs
        self._save_programs_config(self.programs_config)
        
        return new_id
    
    def update_program(self, program_id: int, program_data: Dict[str, Any]):
        """Actualiza un programa existente"""
        programs = self.programs_config.programs
        for i, program in enumerate(programs):
            if program.program_id == program_id:
                program_data["program_id"] = program_id
                programs[i] = ProgramConfig(**program_data)
                break
        
        self.programs_config.programs = programs
        self._save_programs_config(self.programs_config)
    
    def delete_program(self, program_id: int):
        """Elimina un programa"""
        programs = self.programs_config.programs
        programs = [p for p in programs if p.program_id != program_id]
        self.programs_config.programs = programs
        self._save_programs_config(self.programs_config)
    
    def restore_backup(self, backup_file: Path):
        """Restaura una configuración desde un backup"""
        try:
            shutil.copy2(backup_file, APP_CONFIG_FILE)
            # Recargar configuración
            self.app_config = self._load_app_config()
        except Exception as e:
            print(f"Error restaurando backup: {e}")