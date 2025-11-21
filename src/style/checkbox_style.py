from PySide6.QtWidgets import QCheckBox

from .colors import Colors
from .config import StyleConfig


def apply_checkbox_style(checkbox: QCheckBox):
    style = f"""
        QCheckBox::indicator {{
            width: {StyleConfig.Checkbox.SIZE};
            height: {StyleConfig.Checkbox.SIZE};
            border: {StyleConfig.Border.WIDTH} solid {Colors.Checkbox.BORDER};
            border-radius: {StyleConfig.Border.RADIUS_SMALL};
            background: transparent;
        }}

        QCheckBox::indicator:hover {{
            border-color: {Colors.Checkbox.HOVER_BORDER};
        }}

        QCheckBox::indicator:checked {{
            border: {StyleConfig.Border.WIDTH} solid {Colors.Checkbox.CHECKED};
            background: {Colors.Checkbox.CHECKED};
        }}
        QCheckBox::indicator:disabled {{
            border-color: {Colors.Checkbox.DISABLED_BORDER};
            background-color: {Colors.Checkbox.DISABLED_BACKGROUND};
        }}
    """

    checkbox.setStyleSheet(style)
