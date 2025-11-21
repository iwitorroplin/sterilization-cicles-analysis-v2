from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QHBoxLayout,
    QMainWindow,
    QSizePolicy,
    QStackedWidget,
    QVBoxLayout,
    QWidget,
)

from src.core.config import (
    APP_NAME,
    APP_VERSION,
    WINDOW_MIN_HEIGHT,
    WINDOW_MIN_WIDTH,
)
from src.core.module_manager import ModuleManager
from src.ui.widgets.header import HeaderWidget
from src.ui.widgets.footer import FooterWidget
from src.ui.widgets.side_nav import SidebarWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # ❌ Quitar la X de la ventana
        self.setWindowFlag(Qt.WindowCloseButtonHint, False)

        self.setWindowTitle(f"{APP_NAME}  v{APP_VERSION}")
        self.setMinimumSize(WINDOW_MIN_WIDTH, WINDOW_MIN_HEIGHT)

        self.module_manager = ModuleManager()
        self.footer: FooterWidget | None = None

        self._setup_ui()
        self._initialize_modules()

    def _setup_ui(self):
        """Configura la interfaz de usuario."""
        root_container = QWidget()
        root_container.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        app_layout = QVBoxLayout()
        app_layout.setContentsMargins(0, 0, 0, 0)
        app_layout.setSpacing(0)

        app_layout.addWidget(self._create_header(), stretch=0)

        body_widget = QWidget()
        body_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        body_layout = QHBoxLayout()
        body_layout.setContentsMargins(0, 0, 0, 0)
        body_layout.setSpacing(0)

        self.side_nav = self._create_side_nav()
        body_layout.addWidget(self.side_nav, stretch=0)

        self.content_stack = self._create_content_stack()
        body_layout.addWidget(self.content_stack, stretch=1)

        body_widget.setLayout(body_layout)
        app_layout.addWidget(body_widget, stretch=1)

        app_layout.addWidget(self._create_footer(), stretch=0)

        root_container.setLayout(app_layout)
        self.setCentralWidget(root_container)

    def _initialize_modules(self):
        """Carga módulos en el sidebar y muestra el inicial."""
        for module_name in self.module_manager.available_modules:
            self.side_nav.add_module(module_name)

        self.side_nav.add_exit_action()

        if self.module_manager.available_modules:
            initial_module = self.module_manager.available_modules[0]
            self.side_nav.set_active_module(initial_module)

    def _create_header(self) -> HeaderWidget:
        return HeaderWidget()

    def _create_footer(self) -> FooterWidget:
        self.footer = FooterWidget()
        return self.footer

    def _create_side_nav(self) -> SidebarWidget:
        sidebar = SidebarWidget()
        sidebar.module_changed.connect(self._load_module)
        return sidebar

    def _create_content_stack(self) -> QStackedWidget:
        stack = QStackedWidget()
        stack.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        return stack

    def _load_module(self, module_name: str):
        """Carga el módulo solicitado en el área de contenido."""
        module_widget = self.module_manager.get_module(module_name)
        if not module_widget:
            return

        index = self.content_stack.indexOf(module_widget)
        if index == -1:
            self.content_stack.addWidget(module_widget)
            index = self.content_stack.indexOf(module_widget)

        self.content_stack.setCurrentIndex(index)
        self.side_nav.highlight_module(module_name)

        if self.footer:
            self.footer.update_status(f"Módulo activo: {module_name}")
