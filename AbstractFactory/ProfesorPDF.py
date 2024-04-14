from PDF import PDFReport

class ProfesorPDF(PDFReport):
    def generar_reporte(self):
        # Implementación de la generación de reporte de profesores en PDF
        print("Generando reporte de profesores en PDF...")
        print("Datos:", self.data)