from abc import ABC, abstractmethod

# Clase base para los reportes en PDF
class PDFReport(ABC):
    def __init__(self, data):
        self.data = data

    @abstractmethod
    def generar_reporte(self):
        """Generar reportes PDF"""
        
