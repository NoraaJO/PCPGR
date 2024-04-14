from reportFactory import ReportFactory
from estudianteExcel import EstudianteExcel
from EstudiantePDF import EstudiantePDF

class EstudianteFactory(ReportFactory):
    """Fábrica para generar reportes de estudiantes en formato Excel y PDF."""
    def generar_excel(self, data):
        return EstudianteExcel(data)
    
    def generar_pdf(self, data):
        return EstudiantePDF(data)