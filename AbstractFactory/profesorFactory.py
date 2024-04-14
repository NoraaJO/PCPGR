from reportFactory import ReportFactory
from ProfesorPDF import ProfesorPDF
from profesorExcel import ProfesorExcel

class ProfesorFactory(ReportFactory):
    def generar_excel(self, data):
        return ProfesorExcel(data)
    
    def generar_pdf(self, data):
        return ProfesorPDF(data)