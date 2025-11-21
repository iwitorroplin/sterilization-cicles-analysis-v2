"""Configuraciones reutilizables para tipografías, bordes y espaciados."""

class StyleConfig:
    class Font:
        FAMILY = "Segoe UI, Arial, sans-serif"
        SIZE_BASE = "11pt"
        SIZE_SMALL = "10pt"
        SIZE_TITLE = "14pt"
        WEIGHT_NORMAL = "normal"
        WEIGHT_BOLD = "bold"

    class Border:
        WIDTH = "2px"
        WIDTH_THIN = "1px"
        RADIUS = "6px"
        RADIUS_SMALL = "4px"

    class Padding:
        XS = "4px"
        SM = "6px"
        MD = "8px"
        LG = "12px"

    class Layout:
        MAIN_MARGINS = (10, 10, 10, 10)
        MAIN_SPACING = 15
        BUTTON_MARGINS = (0, 10, 0, 0)
        BUTTON_SPACING = 10

    class Checkbox:
        SIZE = "20px"

    class Tab:
        LABEL_PADDING = "6px 14px"
