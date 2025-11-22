from pathlib import Path
from typing import Dict, Any

# Rutas
CONFIG_DIR = Path("config")
DATA_DIR = Path("data")
BACKUP_DIR = CONFIG_DIR / "backups"

# Archivos de configuración
APP_CONFIG_FILE = CONFIG_DIR / "app_config.json"
PROGRAMS_CONFIG_FILE = CONFIG_DIR / "programs_config.json"

# Configuraciones por defecto
DEFAULT_APP_CONFIG: Dict[str, Any] = {
    "general": {
        "printer": "Predeterminada",
        "data_ferlo_dir": "C:/Users/Usuario/Desktop/ferlo",
        "raw_data_ferlo_dir": "C:/Users/Usuario/Desktop/ferlo/raw",
        "process_data_ferlo_dir": "C:/Users/Usuario/Desktop/ferlo/process"
    },
    "cycle_detector": {
        "temperature": 70.0,
        "auto": True,
        "bad_value": "<<<<<<<<"
    }
}

DEFAULT_PROGRAMS_CONFIG: Dict[str, Any] = {
    "programs": [
        {
            "program_id": 1,
            "program_name": "Programa Por Defecto",
            "product_name": "Producto Base",
            "format": "Formato Estándar",
            "target_time": 50.0,
            "target_temperature": 110.0,
            "enabled": True
        }
    ]
}

# Validación
MIN_TEMPERATURE = 0.0
MAX_TEMPERATURE = 300.0
MIN_TIME = 0.0
MAX_TIME = 1000.0