from excelReport import excelReport

class ProfesorExcel(excelReport):
    def generar_reporte(self):
        # Implementación de la generación de reporte de profesores en Excel
        print("Generando reporte de profesores en Excel...")
        print("Datos:", self.data)