import sqlite3

# Conectar a la base de datos
conexion = sqlite3.connect('asistencia.db')
cursor = conexion.cursor()

# Modificar la tabla asistencia_profesores para añadir la columna fecha
try:
    cursor.execute("ALTER TABLE asistencia_profesores ADD COLUMN fecha TEXT")
    print("Columna 'fecha' añadida exitosamente.")
except sqlite3.OperationalError:
    print("La columna 'fecha' ya existe en la tabla 'asistencia_profesores'.")

# Confirmar los cambios y cerrar la conexión
conexion.commit()
conexion.close()
