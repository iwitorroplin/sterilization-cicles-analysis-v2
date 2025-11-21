from typing import Dict, Optional, Type

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QLabel,
    QVBoxLayout,
    QWidget,
)
import importlib

class ModuleManager:
    """Gestor centralizado para módulos con carga bajo demanda"""
    
    _modules_config = {
        "Dashboard": {
            "module_path": "src.ui.mod_dashboard.view",
            "class_name": "ModuleView"
        },
        "Cargar Datos": {
            "module_path": "src.ui.mod_cargar_datos.view", 
            "class_name": "ModuleView"
        },
        "Analizar Ciclos": {
            "module_path": "src.ui.mod_analizar_ciclos.view",
            "class_name": "ModuleView"
        },
        "Programas Ferlo": {
            "module_path": "src.ui.mod_programas_ferlo.view",
            "class_name": "ModuleView"
        },
        "Configuración": {
            "module_path": "src.ui.mod_configuracion.view",
            "class_name": "ModuleView"
        },
        "Ayuda": {
            "module_path": "src.ui.mod_ayuda.view",
            "class_name": "ModuleView"
        }
    }
    
    def __init__(self):
        self._loaded_modules: Dict[str, QWidget] = {}
        self._module_classes: Dict[str, Type[QWidget]] = {}
    
    def get_module(self, module_name: str) -> Optional[QWidget]:
        """Obtiene un módulo (lo carga si es necesario)"""
        if module_name not in self._loaded_modules:
            module = self._load_module(module_name)
            if module:
                self._loaded_modules[module_name] = module
                
        return self._loaded_modules.get(module_name)
    
    def _load_module(self, module_name: str) -> Optional[QWidget]:
        """Carga un módulo dinámicamente"""
        config = self._modules_config.get(module_name)
        if not config:
            print(f"Configuración no encontrada para: {module_name}")
            return None
            
        try:
            # Importar módulo dinámicamente
            module = importlib.import_module(config["module_path"])
            
            # Obtener la clase
            module_class = getattr(module, config["class_name"])
            
            # Crear instancia
            return module_class()
            
        except ImportError as e:
            print(f"Error importando módulo {module_name}: {e}")
            return self._create_fallback_module(module_name)
        except AttributeError as e:
            print(f"Error cargando clase para {module_name}: {e}")
            return self._create_fallback_module(module_name)
        except Exception as e:
            print(f"Error inesperado cargando {module_name}: {e}")
            return self._create_fallback_module(module_name)
    
    def _create_fallback_module(self, module_name: str) -> QWidget:
        """Crea un módulo de respaldo cuando falla la carga"""
        fallback = QWidget()
        layout = QVBoxLayout()
        label = QLabel(f"Módulo '{module_name}' no disponible")
        label.setAlignment(Qt.AlignCenter)
        layout.addWidget(label)
        fallback.setLayout(layout)
        return fallback
    
    def preload_essential_modules(self):
        """Precarga módulos esenciales (opcional)"""
        essential = ["Dashboard"]  # Módulos que quieres cargar al inicio
        for module_name in essential:
            self.get_module(module_name)
    
    def clear_cache(self):
        """Limpia la caché de módulos (útil para liberar memoria)"""
        for module in self._loaded_modules.values():
            if module.parent() is None:  # Solo eliminar si no tiene padre
                module.deleteLater()
        self._loaded_modules.clear()
