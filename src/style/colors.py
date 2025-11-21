"""Color palettes centralizadas para todos los componentes de la UI."""

class Colors:
    class App:
        BACKGROUND = "#1E293B"
        SURFACE = "#1E293B"
        BORDER = "#1E4C18"

    class Text:
        PRIMARY = "#E2E8F0"
        SECONDARY = "#94A3B8"
        INVERTED = "#FFFFFF"
        DISABLED = "#64748B"

    class Label:
        BACKGROUND = "transparent"
        TITLE = "#E2E8F0"
        BODY = "#E2E8F0"
        SUBTLE = "#94A3B8"
        DISABLED = "#64748B"

    class Input:
        BACKGROUND = "#1E293B"
        BORDER = "#334155"
        TEXT = "#E2E8F0"
        PLACEHOLDER_BACKGROUND = "#202B3A"
        PLACEHOLDER_BORDER = "#475569"
        PLACEHOLDER_TEXT = "#94A3B8"
        FOCUS_BORDER = "#3B82F6"

    class ComboBox:
        BACKGROUND = "#1E293B"
        BORDER = "#334155"
        TEXT = "#E2E8F0"
        ARROW = "#CBD5E1"
        FOCUS_BORDER = "#3B82F6"
        HOVER_BORDER = "#475569"
        POPUP_BACKGROUND = "#0F172A"
        POPUP_TEXT = "#E2E8F0"

    class Table:
        BACKGROUND = "#1E293B"
        TEXT = "#E2E8F0"
        BORDER = "#334155"
        GRID = "#475569"
        HEADER_BACKGROUND = "#293548"
        HEADER_TEXT = "#F1F5F9"
        HEADER_BORDER = "#475569"
        ROW_HOVER = "#2C3B4E"
        SELECTION_BACKGROUND = "#3B82F6"
        SELECTION_TEXT = "#FFFFFF"
        CHECKBOX_BORDER = "#48576A"
        CHECKBOX_CHECKED = "#3B82F6"
        CHECKBOX_HOVER = "#5B7290"

    class ButtonPrimary:
        BACKGROUND = "#334155"
        HOVER = "#475569"
        PRESSED = "#0EA5E9"
        CHECKED = "#3B82F6"
        BORDER = "#64748B"
        TEXT = "#FFFFFF"
        
        DISABLED = "#2b2b2b"
        DISABLED_TEXT = "#7c7c7c"
        DISABLED_BORDER = "#3d3d3d"

    class ButtonSecondary:
        BACKGROUND = "#463355"
        HOVER = "#634769"
        PRESSED = "#5B0EE9"
        CHECKED = "#A23BF6"
        BORDER = "#7D648B"
        TEXT = "#FFFFFF"
        
        DISABLED = "#2b2b2b"
        DISABLED_TEXT = "#7c7c7c"
        DISABLED_BORDER = "#3d3d3d"
        
    class ButtonTertiary :
        BACKGROUND = "#1D143A"
        HOVER = "#544769"
        PRESSED = "#0E1DE9"
        CHECKED = "#573BF6"
        BORDER = "#70648B"
        TEXT = "#FFFFFF"
        
        DISABLED = "#2b2b2b"
        DISABLED_TEXT = "#7c7c7c"
        DISABLED_BORDER = "#3d3d3d"

    class ButtonDanger:
        BACKGROUND = "#B91C1C"
        HOVER = "#EC4614"
        PRESSED = "#991B1B"
        CHECKED = "#991B1B"
        BORDER = "#330402"
        TEXT = "#FFFFFF"

    class GroupBox:
        BACKGROUND = "#1E2533"
        BORDER = "#324155"
        TEXT = "#E2E8F0"
        HEADER_BACKGROUND = "#2A3648"
        HEADER_TEXT = "#F8FAFC"

    class Checkbox:
        BORDER = "#E2E8F0"
        HOVER_BORDER = "#475569"
        CHECKED = "#3B82F6"
        DISABLED_BORDER = "#C5D0DF"
        DISABLED_BACKGROUND = "#2c3e50"

    class Status:
        INFO_BACKGROUND = "#e9f3ff"
        INFO_TEXT = "#074a8b"
        INFO_BORDER = "#8ab6e6"

        ERROR_BACKGROUND = "#ffe6e6"
        ERROR_TEXT = "#8b0000"
        ERROR_BORDER = "#d27f7f"

        OK_BACKGROUND = "#e8ffe6"
        OK_TEXT = "#225c1a"
        OK_BORDER = "#7fd27f"

        WARNING_BACKGROUND = "#fff3cd"
        WARNING_TEXT = "#856404"
        WARNING_BORDER = "#ffeaa7"

    class Tab:
        BACKGROUND = "#1E293B"
        BORDER = "#334155"
        TEXT = "#E2E8F0"
        ACTIVE_BACKGROUND = "#3B82F6"
        ACTIVE_TEXT = "#FFFFFF"
        HOVER_BACKGROUND = "#475569"
        DISABLED_TEXT = "#64748B"
        DISABLED_BACKGROUND = "#334155"
