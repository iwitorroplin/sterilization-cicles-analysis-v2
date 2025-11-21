from .colors import Colors
from .config import StyleConfig
from .theme import Theme, get_app_style
from .button_style import apply_button_1_style, apply_button_2_style, apply_button_exit_style
from .checkbox_style import apply_checkbox_style
from .combobox_style import apply_combobox_style
from .groupbox_style import apply_groupbox_style
from .input_style import apply_input_style
from .label_style import apply_label_style
from .layout_style import get_button_layout_config, get_main_layout_config
from .status_style import get_status_style
from .tab_style import apply_tab_style
from .table_style import apply_table_style
from .widget_style import apply_widget_style


class Style:
    colors = Colors
    config = StyleConfig
    theme = Theme

    class button:
        primary = apply_button_1_style
        secondary = apply_button_2_style
        exit = apply_button_exit_style

    class input:
        apply = apply_input_style

    class label:
        apply = apply_label_style
        title = lambda label: apply_label_style(label, "title")
        subtle = lambda label: apply_label_style(label, "subtle")

    class widget:
        apply = apply_widget_style

    class checkbox:
        apply = apply_checkbox_style

    class combobox:
        apply = apply_combobox_style

    class table:
        apply = apply_table_style

    class groupbox:
        apply = apply_groupbox_style

    class tab:
        apply = apply_tab_style

    class layout:
        main = staticmethod(get_main_layout_config)
        buttons = staticmethod(get_button_layout_config)

    class status:
        get_style = staticmethod(get_status_style)

    @staticmethod
    def apply_global(app):
        """Aplica el estilo general a toda la aplicación."""
        app.setStyleSheet(get_app_style())


__all__ = [
    "Colors",
    "StyleConfig",
    "Theme",
    "Style",
    "get_app_style",
    "apply_button_1_style",
    "apply_button_2_style",
    "apply_button_exit_style",
    "apply_checkbox_style",
    "apply_combobox_style",
    "apply_groupbox_style",
    "apply_input_style",
    "apply_label_style",
    "apply_tab_style",
    "apply_table_style",
    "apply_widget_style",
    "get_status_style",
    "get_main_layout_config",
    "get_button_layout_config",
]
