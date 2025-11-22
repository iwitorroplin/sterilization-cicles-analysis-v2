mi_app/
│
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── core/
│   │   ├── __init__.py
│   │   ├── app.py
│   │   ├── router.py
│   │   └── session.py
│   ├── ui/
│   │   ├── __init__.py
│   │   ├── main_window.py
│   │   ├── sidebar.py
│   │   └── widgets/
│   │       ├── __init__.py
│   │       ├── tab_panel.py
│   │       └── validated_input.py
│   ├── modules/
│   │   ├── __init__.py
│   │   ├── base_module.py
│   │   ├── dashboard/
│   │   │   ├── __init__.py
│   │   │   ├── view.py
│   │   │   └── controller.py
│   │   ├── configuracion/
│   │   │   ├── __init__.py
│   │   │   ├── view.py
│   │   │   ├── controller.py
│   │   │   └── models.py
│   │   ├── carga_datos/
│   │   │   ├── __init__.py
│   │   │   ├── view.py
│   │   │   └── controller.py
│   │   ├── analisis/
│   │   │   ├── __init__.py
│   │   │   ├── view.py
│   │   │   └── controller.py
│   │   ├── visualizacion/
│   │   │   ├── __init__.py
│   │   │   ├── view.py
│   │   │   └── controller.py
│   │   └── reportes/
│   │       ├── __init__.py
│   │       ├── view.py
│   │       └── controller.py
│   └── shared/
│       ├── __init__.py
│       ├── constants.py
│       ├── dataclasses.py
│       ├── validators.py
│       └── services/
│           ├── __init__.py
│           ├── config_service.py
│           └── data_service.py
│
├── config/
│   ├── app_config.json
│   └── programs_config.json
│
├── requirements.txt
└── README.md