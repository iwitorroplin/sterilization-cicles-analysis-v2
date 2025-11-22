import pandas as pd
from pathlib import Path
from typing import Optional, Dict, Any
from ..dataclasses import ValidationResult

class DataService:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DataService, cls).__new__(cls)
            cls._instance._initialized = False
        return cls._instance
    
    def __init__(self):
        if self._initialized:
            return
            
        self._current_data: Optional[pd.DataFrame] = None
        self._current_file: Optional[Path] = None
        self._data_metadata: Dict[str, Any] = {}
        
        self._initialized = True
    
    def load_csv(self, file_path: str) -> ValidationResult:
        """Carga datos desde un archivo CSV"""
        result = ValidationResult(is_valid=True)
        
        try:
            file_path_obj = Path(file_path)
            if not file_path_obj.exists():
                result.add_error("El archivo no existe")
                return result
            
            # Leer CSV
            data = pd.read_csv(
                file_path_obj, 
                sep=',',
                encoding='utf-8',
                parse_dates=True,
                infer_datetime_format=True,
                low_memory=False
            )
            
            if data.empty:
                result.add_error("El archivo está vacío")
                return result
            
            # Guardar datos
            self._current_data = data
            self._current_file = file_path_obj
            self._data_metadata = {
                'file_path': str(file_path_obj),
                'rows': len(data),
                'columns': list(data.columns),
                'data_types': dict(data.dtypes)
            }
            
        except Exception as e:
            result.add_error(f"Error leyendo archivo CSV: {str(e)}")
        
        return result
    
    def get_current_data(self) -> Optional[pd.DataFrame]:
        return self._current_data
    
    def get_data_metadata(self) -> Dict[str, Any]:
        return self._data_metadata.copy()
    
    def clear_data(self):
        """Limpia los datos actuales"""
        self._current_data = None
        self._current_file = None
        self._data_metadata = {}