import sqlite3
from datetime import datetime

def conectar():
    return sqlite3.connect('asistencia.db')

def crear_tablas():
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        rol TEXT NOT NULL,  
        correo TEXT UNIQUE NOT NULL,
        contrasena TEXT NOT NULL
    )
    ''')
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS asistencia_profesores (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        profesor TEXT NOT NULL,
        dia_semana TEXT NOT NULL,
        hora_inicio TEXT NOT NULL,
        presente BOOLEAN NOT NULL,
        fecha TEXT NOT NULL
    )
    ''')
    conexion.commit()
    conexion.close()

def crear_usuario(nombre, rol, correo, contrasena):
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute('SELECT * FROM usuarios WHERE correo = ?', (correo,))
    if cursor.fetchone() is None:
        cursor.execute('''
        INSERT INTO usuarios (nombre, rol, correo, contrasena)
        VALUES (?, ?, ?, ?)
        ''', (nombre, rol, correo, contrasena))
        conexion.commit()
    conexion.close()

def registrar_asistencia_profesor(profesor, dia_semana, hora_inicio, presente, fecha=None):
    if fecha is None:
        fecha = datetime.now().strftime('%Y-%m-%d')
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute('''
    INSERT INTO asistencia_profesores (profesor, dia_semana, hora_inicio, presente, fecha)
    VALUES (?, ?, ?, ?, ?)
    ''', (profesor, dia_semana, hora_inicio, presente, fecha))
    conexion.commit()
    conexion.close()

def obtener_usuario(correo, contrasena):
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute('SELECT * FROM usuarios WHERE correo = ? AND contrasena = ?', (correo, contrasena))
    usuario = cursor.fetchone()
    conexion.close()
    return usuario

def obtener_asistencia_por_profesor(profesor, fecha_inicio, fecha_fin):
    conexion = conectar()
    cursor = conexion.cursor()
    query = """
    SELECT profesor, dia_semana, hora_inicio, presente, fecha
    FROM asistencia_profesores
    WHERE profesor = ? AND fecha BETWEEN ? AND ?
    ORDER BY fecha
    """
    cursor.execute(query, (profesor, fecha_inicio, fecha_fin))
    registros = cursor.fetchall()
    conexion.close()
    return registros

def obtener_lista_maestros():
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT DISTINCT nombre FROM usuarios WHERE rol = 'maestro'")
    maestros = [row[0] for row in cursor.fetchall()]
    conexion.close()
    return maestros

def obtener_lista_materias():
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT DISTINCT dia_semana FROM asistencia_profesores")  # Ajusta el campo según la estructura real
    materias = [row[0] for row in cursor.fetchall()]
    conexion.close()
    return materias
