from abc import ABC, abstractmethod

#Clase para reportes Excel
class excelReport(ABC):
    def __init__(self, data):
        self.data = data
    
    @abstractmethod
    def generar_reporte(self):
        """Generar Reporte Excel"""
        