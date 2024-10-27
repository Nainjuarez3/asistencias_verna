import streamlit as st
import database as db
from datetime import datetime, timedelta
import reportes as rp
from database import obtener_lista_maestros, obtener_lista_materias


db.crear_tablas()

# Jefes de grupo
db.crear_usuario("Miguel Ángel Ortiz Torres", "admin", "Miguel@ucol.mx", "Miguel123")  # ICI
db.crear_usuario("Cesar Eduardo Zepeda Gorrocino", "admin", "Cesar@ucol.mx", "Cesar123")  # IME
db.crear_usuario("Michelle Rosales Sánchez", "admin", "Michelle@ucol.mx", "Michelle123")  # IM
db.crear_usuario("Panfilo Gutierrez Alvarez Diaz", "admin", "Panfilo@ucol.mx", "Panfilo123")  # ISET

# Horarios 
horarios_ici = {
    "Lunes": [("09:15", "11:00", "Métodos Numéricos", "David Alejandro Sierra Andrade"),
              ("11:00", "13:00", "Programación Funcional", "Walter Alexander Mata López")],
    "Martes": [("07:00", "08:40", "Sistemas Digitales Embebidos", "Carlos Adrián Bricio Chapula"),
               ("11:00", "13:00", "Interconexión de Redes", "Juan Antonio Diaz Hernández")],
    "Miércoles": [("07:00", "08:40", "Estructura de Datos", "Luis Eduardo Moran López"),
                 ("10:00", "12:00", "Métodos Numéricos", "David Alejandro Sierra Andrade"),
                 ("12:00", "13:00", "Inglés", "Oscar Octavio Ochoa Zúñiga"),
                 ("13:00", "15:00", "Programación Funcional", "Walter Alexander Mata López")],
    "Jueves": [("07:00", "08:40", "Sistemas Digitales Embebidos", "Carlos Adrián Bricio Chapula"),
               ("09:15", "11:00", "Ecuaciones Diferenciales", "Elizabeth Santiago Hernández"),
               ("11:00", "13:00", "Interconexión de Redes", "Juan Antonio Diaz Hernández"),
               ("13:00", "15:00", "Inglés", "Oscar Octavio Ochoa Zúñiga")],
    "Viernes": [("09:15", "11:00", "Ecuaciones Diferenciales", "Elizabeth Santiago Hernández"),
                ("11:00", "12:00", "Métodos Numéricos", "David Alejandro Sierra Andrade"),
                ("13:00", "15:00", "Estructura de Datos", "Luis Eduardo Moran López")]
}

horarios_iset = {
    "Lunes": [("07:00", "08:40", "Ecuaciones Diferenciales", "Vazquez Gonzales Cruz Ernesto"),
              ("09:15", "11:00", "Programación Funcional", "Walter Alexander Mata López"),
              ("12:00", "14:00", "Inglés", "Luis Daniel Benavides Sanches"),
              ("14:00", "15:00", "Métodos Numéricos", "Martines Camera Edgar")],
    "Martes": [("09:15", "11:00", "Ecuaciones Diferenciales", "Vazquez Gonzales Cruz Ernesto"),
               ("11:00", "12:00", "Inglés", "Luis Daniel Benavides Sanches")],
    "Miércoles": [("08:00", "08:40", "Ecuaciones Diferenciales", "Vazquez Gonzales Cruz Ernesto"),
                  ("10:00", "12:00", "Interconexión de Redes", "Juan Antonio Diaz Hernández"),
                  ("12:00", "14:00", "Métodos Numéricos", "Martines Camera Edgar")],
    "Jueves": [("09:15", "11:00", "Sistemas Digitales Embebidos", "Carlos Adrián Bricio Chapula"),
               ("11:00", "13:00", "Estructuras de Datos", "Francisco Manuel Soto Ochoa"),
               ("13:00", "15:00", "Programación Funcional", "Walter Alexander Mata López")],
    "Viernes": [("07:00", "08:40", "Sistemas Digitales Embebidos", "Carlos Adrián Bricio Chapula"),
                ("09:15", "11:00", "Métodos Numéricos", "Martines Camera Edgar"),
                ("11:00", "13:00", "Interconexión de Redes", "Juan Antonio Diaz Hernández")]
}

horarios_ime = {
    "Lunes":[("07:00", "08:40", "Circuitos" , "José Alberto García Jiménez"),
            ("07:00", "8:40", "Circuitos",  "José Alberto García Jiménez"),
            ("09:15", "11:00", "Tecnología de los Materiales", "Selene Cárdenas Rodríguez"),
            ("12:00", "13:00", "Ecuaciones Diferenciales", "Jaime Arroyo Ledesma")],
    "Martes":[("07:00", "08:40", "Electrónica", "José Alberto García Jiménez"),
              ("9:15", "11:00", "Dinámica",  "Sergio Llamas Zamorano"),
              ("11:00", "13:00", "Métodos Numéricos",  "Pablo Armando Alcaraz Valencia"),
              ("13:00", "14:00", "Ecuaciones Diferenciales",  "Jaime Arroyo Ledesma")],
    "Miércoles":[("10:00", "12:00", "Métodos Numéricos",  "Pablo Armando Alcaraz Valencia")], 
     "Jueves":[("07:00", "08:40", "Circuitos", "José Alberto García Jiménez"),
              ("09:15", "11:02",  "Dinámica",  "Sergio Llamas Zamorano"),
              ("11:00", "13:00",  "Ingles",  "Oscar Octavio Ochoa Zúñiga"),
              ("13:00", "14:00",  "Tecnología de los Materiales", "Selene Cárdenas Rodríguez")],
    "Viernes":[("07:00", "08:40",   "Electrónica",  "José Alberto García Jiménez"),
               ("10:00", "11:00",  "Ingles",  "Oscar Octavio Ochoa Zúñiga"),
               ("11:00", "13:00",  "Ecuaciones Diferénciales",  "Jaime Arroyo Ledesma")],

}

horarios_im = {
    "Lunes":[("07:00", "08:00",  "Programacion Web",  "Antonio Alfonso Luis Morales"),
             ("9:15", "11:00", "Aprendizaje de maquina",  "Luis López Moran"), 
             ("12:00",  "14:00",  "Escalamiento de redes", "Oswaldo Carrillo Zepeda")],
    "Martes":[("07:00",  "08:40",  "Ingles",  "Luis Daniel Benavides Sanchez"),
              ("09:15",  "11:00",  "Interacción humano Computadora","Laura Stanley Gaytán Lugo "),
              ("11:00",  "12:00",  "Aprendizaje de maquina",  "Luis López Moran"),
              ("13:00",  "15:00", "Sistemas operativos",  "Apolinar González Potes")],
    "Miercoles":[("9:15", "11:00", "Base de datos no relaciónales",  "Martha Elizabeth Evangelista Salazar"),
                 ("12:00",  "14:00", "Escalamiento de redes", "Oswaldo Carrillo Zepeda")],        
    "Jueves":[("07:00" ,"08:40", "Programación web",  "Antonio Alfonso Luis Morales"),
              ("10:00", "11:00", "Ingles", "Luis Daniel Benavides Sanchez"),
              ("12:00", "14:00",  "Aprendizaje de maquina",   "Luis López Moran")], 
    "Viernes":[("09:15", "11:00", "Sistemas operativos",  "Apolinar González Potes"),
               ("11:00",  "13:00",  "Base de datos no relacionales",   "Martha Elizabeth Evangelista Salazar"),
               ("13: 00",  "15:00",  "Interacción humana computadora",   "Laura Stanley Gaytán Lugo")] 


}

# Función para login de usuario
def login(correo, contrasena):
    return db.obtener_usuario(correo, contrasena)

# Mostrar horarios de cada carrera
def mostrar_horarios(carrera, dia_semana):
    st.write(f"Mostrando horarios para {dia_semana} de la carrera {carrera}")  
    horarios = []
    if carrera == "ICI":
        horarios = horarios_ici.get(dia_semana, [])
    elif carrera == "ISET":
        horarios = horarios_iset.get(dia_semana, [])
    elif carrera == "IME":
        horarios = horarios_ime.get(dia_semana, [])
    elif carrera == "IM":
        horarios = horarios_im.get(dia_semana, [])

    if not horarios:
        st.warning(f"No hay horarios disponibles para {dia_semana}.")
        return

    for hora_inicio, hora_fin, materia, profesor in horarios:
        col_horario, col_materia, col_asistencia = st.columns([1, 3, 1])
        col_horario.write(f"{hora_inicio} - {hora_fin}")
        col_materia.markdown(f"**{materia} - {profesor}**")
        asistencia = col_asistencia.checkbox(f"Asistió", key=f"{dia_semana}-{hora_inicio}-{hora_fin}")
        if st.button(f"Registrar ({hora_inicio}-{hora_fin})", key=f"btn-{dia_semana}-{hora_inicio}-{hora_fin}"):
            presente = True if asistencia else False
            db.registrar_asistencia_profesor(profesor, dia_semana, hora_inicio, presente, datetime.now().strftime('%Y-%m-%d'))
            st.success(f"Asistencia registrada para {materia}.")

# Función para el panel del jefe de grupo
def admin_menu(usuario):
    st.header(f"Panel de Asistencia - {usuario[1]}")

    # Muestra la selección de horarios como en la implementación original
    fecha_seleccionada = st.date_input("Selecciona un día", value=datetime.today(), min_value=datetime.today() - timedelta(days=30), max_value=datetime.today() + timedelta(days=30))
    dia_semana = fecha_seleccionada.strftime("%A")  
    dias_semana_traducidos = {
        "Monday": "Lunes",
        "Tuesday": "Martes",
        "Wednesday": "Miércoles",
        "Thursday": "Jueves",
        "Friday": "Viernes",
        "Saturday": "Sábado",
        "Sunday": "Domingo"
    }
    dia_semana_es = dias_semana_traducidos.get(dia_semana, dia_semana)  


    # Determina la carrera del administrador para filtrar los reportes
    carrera = ""
    if usuario[1] == "Miguel Ángel Ortiz Torres":
        carrera = "ICI"
        mostrar_horarios("ICI", dia_semana_es)
    elif usuario[1] == "Cesar Eduardo Zepeda Gorrocino":
        carrera = "IME"
        mostrar_horarios("IME", dia_semana_es)
    elif usuario[1] == "Michelle Rosales Sánchez":
        carrera = "IM"
        mostrar_horarios("IM", dia_semana_es)
    elif usuario[1] == "Panfilo Gutierrez Alvarez Diaz":
        carrera = "ISET"
        mostrar_horarios("ISET", dia_semana_es)

    # Nueva sección para generación de reportes de asistencia
    st.subheader("Generación de Reportes de Asistencia")
    reporte_tipo = st.selectbox("Selecciona el tipo de reporte:", ["Por Profesor", "Por Materia", "Estadísticas Globales"])
    
    # Rango de fechas para el reporte
    fecha_inicio = st.date_input("Fecha de inicio para el reporte", value=datetime.today() - timedelta(days=7))
    fecha_fin = st.date_input("Fecha de fin para el reporte", value=datetime.today())

    if reporte_tipo == "Por Profesor":
        # Desplegable de maestros
        lista_maestros = obtener_lista_maestros()
        profesor = st.selectbox("Selecciona el profesor para el reporte:", lista_maestros)
        if st.button("Generar Reporte por Profesor"):
            rp.generar_reporte_por_profesor(profesor, fecha_inicio.strftime('%Y-%m-%d'), fecha_fin.strftime('%Y-%m-%d'))
            st.success(f"Reporte de asistencia generado para el profesor {profesor}.")

    elif reporte_tipo == "Por Materia":
        # Desplegable de materias
        lista_materias = obtener_lista_materias()
        materia = st.selectbox("Selecciona la materia para el reporte:", lista_materias)
        if st.button("Generar Reporte por Materia"):
            rp.generar_reporte_por_materia(materia, fecha_inicio.strftime('%Y-%m-%d'), fecha_fin.strftime('%Y-%m-%d'))
            st.success(f"Reporte de asistencia generado para la materia {materia}.")

    elif reporte_tipo == "Estadísticas Globales":
        if st.button("Generar Estadísticas Globales"):
            rp.generar_estadisticas_globales(carrera, fecha_inicio.strftime('%Y-%m-%d'), fecha_fin.strftime('%Y-%m-%d'))
            st.success(f"Reporte de estadísticas globales generado para la carrera {carrera}.")

# Función para el menú de maestros
def menu_maestro(usuario):
    st.header(f"Panel de Asistencia - {usuario[1]} (Maestro)")
    fecha_inicio = st.date_input("Fecha de inicio", value=datetime.today() - timedelta(days=7))
    fecha_fin = st.date_input("Fecha de fin", value=datetime.today())
    if st.button("Descargar Reporte de Asistencia en PDF"):
        rp.generar_reporte_profesor(usuario[1], fecha_inicio.strftime('%Y-%m-%d'), fecha_fin.strftime('%Y-%m-%d'))
        st.success("Reporte descargado con éxito.")

# Login
if 'usuario' not in st.session_state:
    st.session_state['usuario'] = None

if st.session_state['usuario'] is None:
    st.title("Sistema de Gestión de Asistencias")
    correo = st.text_input("Correo")
    contrasena = st.text_input("Contraseña", type="password")
    if st.button("Iniciar sesión"):
        usuario = login(correo, contrasena)
        if usuario:
            st.session_state['usuario'] = usuario
        else:
            st.error("Credenciales incorrectas")
else:
    usuario = st.session_state['usuario']
    st.success(f"Bienvenido {usuario[1]} ({usuario[2]})")
    if usuario[2] == "admin":
        admin_menu(usuario)
    elif usuario[2] == "maestro":
        menu_maestro(usuario)

if st.session_state['usuario'] is not None:
    if st.button("Cerrar sesión"):
        st.session_state['usuario'] = None

