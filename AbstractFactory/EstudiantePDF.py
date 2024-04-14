from PDF import PDFReport

class EstudiantePDF(PDFReport):
    """Generar PDF estudiante"""
    def generar_reporte(self):
        """Implementación de la generación de reporte de estudiantes en PDF"""
        print("Generando reporte de estudiantes en PDF...")
        print("Datos:", self.data)