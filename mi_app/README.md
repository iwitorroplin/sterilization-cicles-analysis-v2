# mi_app

Sistema de referencia para analizar ciclos de esterilización con una arquitectura de módulos clara y desacoplada.

## Arquitectura
- **core**: infraestructura compartida (enrutador, sesión, bootstrap de la ventana principal).
- **modules**: cada funcionalidad se encapsula en un módulo con controlador y vista independientes.
- **ui**: componentes comunes y estilos (QSS) aplicables en todas las pantallas.
- **shared**: modelos, validadores y servicios reutilizables (configuración, datos).

## Módulos clave
- **Dashboard**: muestra el estado general (archivo cargado, métricas básicas y rutas de configuración).
- **Carga de Datos**: asistente para abrir CSV, validar contenido y guardar metadatos y vista previa.
- **Análisis**: calcula estadísticas rápidas sobre los datos numéricos disponibles.
- **Visualización**: plantilla para incorporar gráficos o dashboards personalizados.
- **Reportes**: punto de entrada para generar informes basados en los datos cargados.
- **Configuración**: edición de rutas, parámetros del detector de ciclos y catálogo de programas.

## Conceptos compartidos
- **Session**: singleton ligero que centraliza servicios (`ConfigService`, `DataService`) y estado transversal.
- **Router**: orquesta la navegación entre módulos y emite señales para sincronizar la UI.
- **BaseModule**: interfaz mínima que garantiza que cada módulo exponga `view()` y el *hook* `on_activate()`.
- **Servicios**: `ConfigService` gestiona archivos JSON de configuración con copias de seguridad; `DataService` carga y conserva los datos en memoria junto con su metadata.
- **Estilos**: la carpeta `ui/styles` concentra la paleta y el *stylesheet* base aplicable a la interfaz completa.
