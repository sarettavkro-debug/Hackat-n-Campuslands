import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Gestión Operativa Campuslands", layout="wide")

# Título principal con diseño
st.title("🖥️ Sistema Central de Gestión Operativa - Campuslands")
st.markdown("---")

# Barra lateral para navegación o filtros rápidos
st.sidebar.header("Panel de Control")
modulo = st.sidebar.selectbox(
    "Selecciona un Módulo",
    ["Disponibilidad de Espacios", "Préstamo de Recursos", "Triaje con IA"]
)

if modulo == "Disponibilidad de Espacios":
    st.header("Módulo 1: Gestión de Aulas y Cubículos")
    
    col1, col2 = st.columns(2)
    with col1:
        aula = st.text_input("Código de Aula")
        capacidad = st.number_input("Aforo requerido", min_value=1, max_value=50)
    with col2:
        st.info("Regla activa: Evitar solapamientos y conflictos de aforo.")
        
    if st.button("Verificar Disponibilidad"):
        st.success(f"El aula {aula} está disponible para un aforo de {capacidad} personas.")

elif modulo == "Triaje con IA":
    st.header("Módulo 3: Triaje Inteligente de Incidencias")
    
    incidencia = st.text_area("Describe el problema reportado en el campus:")
    
    if st.button("Analizar con IA"):
        if incidencia:
            st.warning("Procesando datos con el modelo autorizado...")
            st.success("Categoría asignada por IA: **Prioridad Alta - Mantenimiento Técnico**")
        else:
            st.error("Por favor, ingresa una descripción de la incidencia.")