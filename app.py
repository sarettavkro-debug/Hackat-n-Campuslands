import streamlit as st

st.set_page_config(
    page_title="Sistema Central de Gestión Operativa",
    page_icon="🏫",
    layout="wide"
)

st.title("🖥️ Sistema Central de Gestión Operativa - Campuslands")
st.markdown("---")

st.sidebar.header("Panel de Navegación")
modulo_seleccionado = st.sidebar.selectbox(
    "Seleccione un módulo:",
    [
        "1. Disponibilidad de Espacios",
        "2. Préstamo de Recursos",
        "3. Triaje de Incidencias"
    ]
)

if modulo_seleccionado == "1. Disponibilidad de Espacios":
    st.header("Módulo de Disponibilidad de Espacios")
    st.write("Aquí gestionaremos las aulas y cubículos evitando solapamientos y aforos excedidos[cite: 2].")

    col1, col2 = st.columns(2)
    with col1:
        st.text_input("Código de Aula / Cubículo")
    with col2:
        st.number_input("Número de personas (Aforo)", min_value=1, max_value=100)

    if st.button("Verificar Espacio"):
        st.info("Función de validación en desarrollo...")

elif modulo_seleccionado == "2. Préstamo de Recursos":
    st.header("Módulo de Préstamo de Recursos")
    st.write("Control y trazabilidad de los equipos tecnológicos del campus[cite: 2].")

    st.selectbox("Seleccione el equipo tecnológico:", ["Proyector", "Laptop HP", "Tablet"])
    if st.button("Registrar Préstamo"):
        st.success("Préstamo registrado correctamente (simulación).")

elif modulo_seleccionado == "3. Triaje de Incidencias":
    st.header("Módulo de Triaje de Incidencias con IA")
    st.write("Clasificación y priorización automatizada de solicitudes[cite: 2].")

    st.text_area("Describa la incidencia reportada:")
    if st.button("Analizar Incidencia"):
        st.warning("Enviando datos al modelo de IA...")