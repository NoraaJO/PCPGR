from abc import ABC, abstractmethod

# Interfaz para las fábricas de reportes
class ReportFactory(ABC):
    """Clase Interfaz que generar los reportes"""
    @abstractmethod
    def generar_excel(self, data):
        """Generar Reporte Excel"""
        
    
    @abstractmethod
    def generar_pdf(self, data):
        """Generar Reporte PDF"""
        