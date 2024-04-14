from excelReport import excelReport

class EstudianteExcel(excelReport):
    def generar_reporte(self):
        # Implementación de la generación de reporte de estudiantes en Excel
        print("Generando reporte de estudiantes en Excel...")
        print("Datos:", self.data)