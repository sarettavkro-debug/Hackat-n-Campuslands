import streamlit as st


from models.campus_logic import validar_aforo_espacio, cargar_datos

st.set_page_config(page_title="Gestión Operativa - Campuslands", layout="wide")
st.title("🏫 Sistema Central de Gestión Operativa - Campuslands")

modulo = st.sidebar.selectbox("Selecciona un Módulo:", ["1. Disponibilidad de Espacios", "2. Préstamo de Recursos", "3. Triaje con IA"])

if modulo == "1. Disponibilidad de Espacios":
    st.header("🏢 Módulo 1: Gestión de Aulas y Cubículos")
    
    # 2. Usamos los datos reales que cargó la Persona 1 para llenar el selectbox dinámicamente
    datos_actuales = cargar_datos()
    nombres_espacios = [e["codigo"] for e in datos_actuales.get("espacios", [])]
    
    col1, col2 = st.columns(2)
    with col1:
        aula_seleccionada = st.selectbox("Seleccione el Aula", nombres_espacios)
        capacidad = st.number_input("Aforo requerido", min_value=1, max_value=100, value=10)
    with col2:
        st.info("💡 Validación conectada con la lógica de negocio.")
        
    # 3. Al hacer clic, llamamos a la función de la Persona 1 para validar de verdad
    if st.button("🔍 Verificar Disponibilidad", use_container_width=True):
        valido, mensaje = validar_aforo_espacio(aula_seleccionada, capacidad)
        if valido:
            st.success(mensaje)
        else:
            st.error(mensaje)

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

if modulo == "1. Disponibilidad de Espacios":
    st.header("🏢 Módulo 1: Gestión de Aulas y Cubículos")
    st.write("Verifica disponibilidad de espacios asegurando cumplimiento de aforo máximo.")

    col1, col2 = st.columns(2)
    
    with col1:
        aula = st.text_input("Código o Nombre del Aula / Cubículo", placeholder="Ej: Aula-101")
        capacidad = st.number_input("Aforo requerido (personas)", min_value=1, max_value=60, value=10)
    
    with col2:
        st.info("💡 **Regla activa:** Previene sobrecupos y garantiza disponibilidad por capacidad.")
        
    if st.button("🔍 Verificar Disponibilidad", use_container_width=True):
        if aula.strip() == "":
            st.warning("⚠️ Por favor ingresa el código del aula o cubículo.")
        else:
            # Conexión futura con lógica del backend (Persona 1)
            st.success(f"✅ El aula **{aula}** está disponible para un aforo de **{capacidad}** personas.")

elif modulo == "2. Préstamo de Recursos":
    st.header("📦 Módulo 2: Control y Préstamo de Recursos")
    st.write("Gestiona la asignación y estado del material tecnológico del campus.")

    col1, col2 = st.columns(2)

    with col1:
        equipo = st.selectbox(
            "Selecciona el equipo tecnológico:",
            ["Proyector HD", "Laptop Core i7", "Tablet Gráfica", "Kit de Cableado HDMI"]
        )
        usuario = st.text_input("Nombre / Documento del Solicitante", placeholder="Ej: Juan Pérez")

    with col2:
        st.info("💡 **Regla activa:** Registra trazabilidad de salida e impide préstamo de equipos no disponibles.")

    if st.button("📋 Registrar Préstamo", use_container_width=True):
        if usuario.strip() == "":
            st.error("❌ Se requiere el nombre o documento del solicitante.")
        else:
            # Conexión futura con lógica de inventario (Persona 1)
            st.success(f"🎉 Préstamo registrado: **{equipo}** asignado exitosamente a **{usuario}**.")

elif modulo == "3. Triaje con IA":
    st.header("🤖 Módulo 3: Triaje Inteligente de Incidencias")
    st.write("Reporta incidentes del campus para priorización y análisis automatizado.")

    incidencia = st.text_area(
        "Describe el problema reportado:",
        placeholder="Ej: El aire acondicionado del laboratorio 2 presenta fallas de enfriamiento...",
        height=120
    )

    if st.button("⚡ Analizar e Indicar Prioridad", use_container_width=True):
        if incidencia.strip() == "":
            st.error("⚠️ Por favor, ingresa una descripción detallada de la incidencia.")
        else:
            # Conexión futura con el modelo de IA (Persona 2)
            st.warning("🔄 Procesando solicitud con el servicio de IA...")
            
            # Simulación visual del resultado
            st.markdown("---")
            st.subheader("📊 Resultado del Triaje:")
            st.success("🚨 **Categoría Asignada:** Mantenimiento Técnico | **Prioridad:** Alta")