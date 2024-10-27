from fpdf import FPDF
from database import obtener_asistencia_por_profesor, conectar

def generar_reporte_por_profesor(profesor, fecha_inicio, fecha_fin):
    registros = obtener_asistencia_por_profesor(profesor, fecha_inicio, fecha_fin)
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('Arial', 'B', 16)
    pdf.cell(200, 10, f'Reporte de Asistencia para {profesor}', ln=True, align='C')
    pdf.ln(10)
    pdf.set_font('Arial', 'B', 12)
    pdf.cell(50, 10, 'Fecha', 1)
    pdf.cell(50, 10, 'Día Semana', 1)
    pdf.cell(50, 10, 'Hora Inicio', 1)
    pdf.cell(40, 10, 'Asistencia', 1)
    pdf.ln()
    pdf.set_font('Arial', '', 12)
    for registro in registros:
        fecha = registro[4]
        dia_semana = registro[1]
        hora_inicio = registro[2]
        presente = "Sí" if registro[3] else "No"
        pdf.cell(50, 10, fecha, 1)
        pdf.cell(50, 10, dia_semana, 1)
        pdf.cell(50, 10, hora_inicio, 1)
        pdf.cell(40, 10, presente, 1)
        pdf.ln()
    pdf.output(f'reporte_asistencia_{profesor}_{fecha_inicio}_a_{fecha_fin}.pdf')

def generar_reporte_por_materia(materia, fecha_inicio, fecha_fin):
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("""
        SELECT profesor, COUNT(*) AS total_clases, SUM(CASE WHEN presente = 1 THEN 1 ELSE 0 END) AS clases_asistidas
        FROM asistencia_profesores
        WHERE dia_semana = ? AND fecha BETWEEN ? AND ?
        GROUP BY profesor
    """, (materia, fecha_inicio, fecha_fin))
    registros = cursor.fetchall()
    conexion.close()

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('Arial', 'B', 16)
    pdf.cell(200, 10, f'Reporte de Asistencia por Materia: {materia}', ln=True, align='C')
    pdf.ln(10)
    pdf.set_font('Arial', 'B', 12)
    pdf.cell(60, 10, 'Profesor', 1)
    pdf.cell(40, 10, 'Total Clases', 1)
    pdf.cell(40, 10, 'Clases Asistidas', 1)
    pdf.cell(40, 10, 'Porcentaje', 1)
    pdf.ln()
    pdf.set_font('Arial', '', 12)
    for profesor, total_clases, clases_asistidas in registros:
        porcentaje = f"{(clases_asistidas / total_clases) * 100:.2f}%" if total_clases > 0 else "0%"
        pdf.cell(60, 10, profesor, 1)
        pdf.cell(40, 10, str(total_clases), 1)
        pdf.cell(40, 10, str(clases_asistidas), 1)
        pdf.cell(40, 10, porcentaje, 1)
        pdf.ln()
    pdf.output(f'reporte_asistencia_materia_{materia}_{fecha_inicio}_a_{fecha_fin}.pdf')

def generar_estadisticas_globales(carrera, fecha_inicio, fecha_fin):
    """
    Genera un reporte en PDF de estadísticas globales de asistencia por carrera.
    
    Parameters:
    carrera (str): Nombre de la carrera (ICI, IME, ISET, IM) para filtrar el reporte.
    fecha_inicio (str): Fecha de inicio en formato 'YYYY-MM-DD'.
    fecha_fin (str): Fecha de fin en formato 'YYYY-MM-DD'.
    """
    conexion = conectar()
    cursor = conexion.cursor()
    query = """
        SELECT profesor, COUNT(*) AS total_clases, SUM(CASE WHEN presente = 1 THEN 1 ELSE 0 END) AS clases_asistidas, rol
        FROM asistencia_profesores 
        JOIN usuarios ON asistencia_profesores.profesor = usuarios.nombre
        WHERE usuarios.rol = ? AND fecha BETWEEN ? AND ?
        GROUP BY profesor
    """
    cursor.execute(query, (carrera, fecha_inicio, fecha_fin))
    registros = cursor.fetchall()
    conexion.close()

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('Arial', 'B', 16)
    pdf.cell(200, 10, f'Estadísticas Globales de Asistencia para {carrera}', ln=True, align='C')
    pdf.ln(10)
    pdf.set_font('Arial', 'B', 12)
    pdf.cell(60, 10, 'Profesor', 1)
    pdf.cell(40, 10, 'Total Clases', 1)
    pdf.cell(40, 10, 'Clases Asistidas', 1)
    pdf.cell(40, 10, 'Porcentaje', 1)
    pdf.cell(40, 10, 'Rol', 1)
    pdf.ln()
    pdf.set_font('Arial', '', 12)
    for profesor, total_clases, clases_asistidas, rol in registros:
        porcentaje = f"{(clases_asistidas / total_clases) * 100:.2f}%" if total_clases > 0 else "0%"
        pdf.cell(60, 10, profesor, 1)
        pdf.cell(40, 10, str(total_clases), 1)
        pdf.cell(40, 10, str(clases_asistidas), 1)
        pdf.cell(40, 10, porcentaje, 1)
        pdf.cell(40, 10, rol, 1)
        pdf.ln()
    pdf.output(f'estadisticas_globales_{carrera}_{fecha_inicio}_a_{fecha_fin}.pdf')
