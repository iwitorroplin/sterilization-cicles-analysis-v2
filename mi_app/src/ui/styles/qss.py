from __future__ import annotations

from . import palette


def app_stylesheet() -> str:
    return f"""
        QWidget {{
            background: {palette.BACKGROUND};
            color: {palette.TEXT};
            font-size: 13px;
        }}

        QGroupBox {{
            border: 1px solid {palette.BORDER};
            border-radius: 6px;
            margin-top: 12px;
            background: {palette.SURFACE};
        }}

        QGroupBox::title {{
            subcontrol-origin: margin;
            left: 10px;
            padding: 0 3px 0 3px;
            color: {palette.SECONDARY};
            font-weight: bold;
        }}

        QPushButton {{
            background: {palette.PRIMARY};
            color: white;
            border: none;
            border-radius: 6px;
            padding: 8px 14px;
        }}

        QPushButton:disabled {{
            background: {palette.BORDER};
            color: {palette.MUTED};
        }}

        QPushButton:hover:!disabled {{
            background: #0C6EDC;
        }}

        QPushButton:checked {{
            background: {palette.SECONDARY};
        }}

        QLineEdit, QComboBox, QSpinBox, QDoubleSpinBox {{
            background: white;
            border: 1px solid {palette.BORDER};
            border-radius: 4px;
            padding: 6px;
        }}

        QTableWidget {{
            background: white;
            border: 1px solid {palette.BORDER};
            gridline-color: {palette.BORDER};
        }}
    """
