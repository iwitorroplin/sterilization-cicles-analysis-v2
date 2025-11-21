from PySide6.QtCore import QThread, Signal
from ..ui.widgets.loading_dialog import LoadingDialog

class WorkerThread(QThread):
    """Hilo worker para ejecutar procesos pesados"""
    finished = Signal()
    
    def __init__(self, func, args=None):
        super().__init__()
        self.func = func
        self.args = args if args else []
    
    def run(self):
        try:
            if callable(self.func):
                self.func(*self.args)
        finally:
            self.finished.emit()

class LoadingManager:
    """Gestor para manejar múltiples procesos de carga en serie"""
    
    def __init__(self, parent=None):
        self.parent = parent
        self.loading_dialog = None
        self.current_process = 0
        self.processes = []
    
    def start_loading(self, processes, on_finished=None):
        """
        Inicia una serie de procesos de carga

        Args:
            processes: Lista de tuplas (texto, función, args)
            on_finished: Callback a ejecutar cuando finalizan todos los procesos
        """
        self.processes = processes
        self.current_process = 0
        self.on_finished = on_finished

        self.loading_dialog = LoadingDialog(self.parent)
        self.loading_dialog.show()
        self.execute_next_process()
    
    def execute_next_process(self):
        """Ejecuta el siguiente proceso en la lista"""
        if self.current_process < len(self.processes):
            text, func, args = self.processes[self.current_process]
            self.loading_dialog.update_text(text)
            
            self.worker_thread = WorkerThread(func, args)
            self.worker_thread.finished.connect(self.on_process_finished)
            self.worker_thread.start()
        else:
            self.loading_dialog.fade_out_and_close()
            if callable(self.on_finished):
                self.on_finished()
    
    def on_process_finished(self):
        """Se llama cuando un proceso termina"""
        self.current_process += 1
        self.execute_next_process()