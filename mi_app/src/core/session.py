from shared.services.config_service import ConfigService
from shared.services.data_service import DataService

class Session:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Session, cls).__new__(cls)
            cls._instance._initialized = False
        return cls._instance
    
    def __init__(self):
        if self._initialized:
            return
            
        # Servicios
        self.config_service = ConfigService()
        self.data_service = DataService()
        
        # Estado de la aplicación
        self.current_module = None
        self.loaded_data = None
        self.analysis_results = None
        self.current_program = None
        
        self._initialized = True
    
    def get_config_service(self) -> ConfigService:
        return self.config_service
    
    def get_data_service(self) -> DataService:
        return self.data_service