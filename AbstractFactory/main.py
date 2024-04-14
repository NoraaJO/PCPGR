from estudianteFactory import EstudianteFactory
from profesorFactory import ProfesorFactory

if __name__ == "__main__":
    # Datos de ejemplo
    datos_estudiante = {
        "Nombre": "Juan",
        "Apellido": "Perez",
        "Carnet": "123456",
        "Correo": "juanp@estudiantec.cr",
        "Sede": "Cartago",
        "Teléfono": "123456789",
        "Ponderado Actual": 80.5
    }

    datos_profesor = {
        "Nombre": "María",
        "Apellido": "González",
        "Cedula": "123456789",
        "Correo": "mariag@itcr.ac.cr",
        "Sede": "Cartago",
        "Oficina": "A101",
        "Teléfono": "987654321",
        "Curso": "Programación Avanzada"
    }

    # Crear fábricas de reportes
    estudiante_factory = EstudianteFactory()
    profesor_factory = ProfesorFactory()

    # Generar reportes de estudiantes
    estudiante_excel = estudiante_factory.generar_excel(datos_estudiante)
    estudiante_excel.generar_reporte()

    estudiante_pdf = estudiante_factory.generar_pdf(datos_estudiante)
    estudiante_pdf.generar_reporte()

    # Generar reportes de profesores
    profesor_excel = profesor_factory.generar_excel(datos_profesor)
    profesor_excel.generar_reporte()

    profesor_pdf = profesor_factory.generar_pdf(datos_profesor)
    profesor_pdf.generar_reporte()
