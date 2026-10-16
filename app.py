import streamlit as st
import os
from dotenv import load_dotenv

# Importar la lógica de negocio y persistencia desde models/campus_logic.py
try:
    from models.campus_logic import (
        listar_espacios,
        buscar_espacio,
        validar_capacidad,
        validar_disponibilidad_espacio,
        validar_recurso_para_prestamo,
        actualizar_estado_espacio
    )
except ImportError:
    def listar_espacios(): return []
    def buscar_espacio(id_espacio): return None
    def validar_capacidad(id_espacio, cant): return False, "Módulo de lógica no encontrado."
    def validar_disponibilidad_espacio(id): return False, "No disponible."

# Importar el manejador de IA desde ai_service/ia_handler.py
try:
    from ai_service.ia_handler import procesar_triaje_con_ia
except ImportError:
    def procesar_triaje_con_ia(texto):
        return {"error": "Módulo de IA no conectado correctamente."}

# Cargar variables de entorno de forma segura
load_dotenv()

# Configuración inicial de la página
st.set_page_config(
    page_title="Sistema Central de Gestión Operativa - Campuslands",
    page_icon="🏫",
    layout="wide"
)

# Estilos CSS personalizados (Paleta de colores optimizada y componentes mejorados)
st.markdown("""
    <style>
    .stApp {
        background-color: #1C1F26;
        color: #FFFFFF;
    }
    
    /* Contenedores y tarjetas estéticas */
    div[data-testid="stVerticalBlock"] > div[style*="background-color"] {
        border-radius: 12px;
        border: 1px solid #33373E;
    }

    /* Botones principales */
    .stButton > button {
        background-color: #6B5BFF;
        color: #FFFFFF;
        border-radius: 8px;
        border: none;
        font-weight: bold;
        padding: 10px 20px;
        width: 100%;
        transition: background-color 0.2s ease;
    }
    .stButton > button:hover {
        background-color: #5548e0;
        color: #FFFFFF;
    }

    /* Tipografía institucional */
    h1, h2, h3 {
        color: #FFFFFF !important;
    }
    
    /* Personalización de la barra lateral (Sidebar) */
    section[data-testid="stSidebar"] {
        background-color: #16181D;
        border-right: 1px solid #33373E;
    }
    </style>
""", unsafe_allow_html=True)

# Título principal del sistema operativo del campus
st.title("🖥️ Sistema Central de Gestión Operativa — Campuslands")
st.markdown("<p style='color: #00D2D3; font-weight: bold;'>Plataforma MVP Integrada con IA • Protocolo PSA-9</p>", unsafe_allow_html=True)
st.markdown("---")

# ---------------------------------------------------------
# MENÚ LATERAL (SIDEBAR) MEJORADO VISUALMENTE
# ---------------------------------------------------------
with st.sidebar:
    st.markdown("### 🏫 Panel de Control")
    st.markdown("<p style='color: #8c929d; font-size: 13px; margin-top: -10px;'>Seleccione un módulo operativo:</p>", unsafe_allow_html=True)
    st.markdown("---")
    
    modulo_seleccionado = st.radio(
        "Navegación principal",
        [
            "1. Disponibilidad de Espacios",
            "2. Préstamo de Recursos",
            "3. Triaje de Incidencias"
        ],
        label_visibility="collapsed"
    )
    
    st.markdown("---")
    st.markdown("<div style='background-color: #33373E; padding: 12px; border-radius: 8px; font-size: 12px;'>🟢 <b>Estado del Sistema:</b><br>Nodo operativo v2.6 activo.</div>", unsafe_allow_html=True)

# ---------------------------------------------------------
# MÓDULO 1: Disponibilidad y Asignación de Espacios
# ---------------------------------------------------------
if modulo_seleccionado == "1. Disponibilidad de Espacios":
    st.header("🏢 Módulo 1: Disponibilidad y Asignación de Espacios")
    st.write("Control en tiempo real de aulas y cubículos para evitar solapamientos y conflictos de aforo.")

    espacios = listar_espacios()
    opciones_espacios = {f"{esp['id']} - {esp['nombre']} (Capacidad: {esp['capacidad']})": esp['id'] for esp in espacios}

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("<div style='background-color: #33373E; padding: 20px; border-radius: 10px;'>", unsafe_allow_html=True)
        st.subheader("Criterios de Verificación")
        
        espacio_seleccionado_txt = st.selectbox("Seleccione un espacio del campus", list(opciones_espacios.keys()) if opciones_espacios else ["No hay espacios cargados"])
        id_actual = opciones_espacios.get(espacio_seleccionado_txt) if opciones_espacios else None
        
        aforo_requerido = st.number_input("Cantidad de personas (Aforo requerido)", min_value=1, max_value=200, value=10)
        verificar_btn = st.button("Verificar Reglas de Negocio")
        st.markdown("</div>", unsafe_allow_html=True)

    with col2:
        st.markdown("<div style='background-color: #33373E; padding: 20px; border-radius: 10px;'>", unsafe_allow_html=True)
        st.subheader("Resultado de Validación")

        if verificar_btn and id_actual:
            disp_ok, disp_msg = validar_disponibilidad_espacio(id_actual)
            cap_ok, cap_msg = validar_capacidad(id_actual, aforo_requerido)

            if disp_ok and cap_ok:
                st.success("✅ **Validación Exitosa:**")
                st.markdown(f"- {disp_msg}")
                st.markdown(f"- {cap_msg}")
                st.markdown("<span style='color: #00D2D3; font-weight: bold;'>● Estado: Asignación permitida sin solapamientos.</span>", unsafe_allow_html=True)
            else:
                st.error("❌ **Conflicto Detectado (Regla de Negocio):**")
                if not disp_ok: st.markdown(f"- {disp_msg}")
                if not cap_ok: st.markdown(f"- {cap_msg}")
                st.markdown("<span style='color: #F3C64A; font-weight: bold;'>● Estado: Asignación rechazada por la política del campus.</span>", unsafe_allow_html=True)
        else:
            st.info("ℹ️ Seleccione un espacio, ingrese el aforo y presione el botón para ejecutar las validaciones del sistema.")
            st.markdown("<span style='color: #00D2D3; font-weight: bold;'>● Estado del Nodo: Activo</span>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

# ---------------------------------------------------------
# MÓDULO 2: Préstamo y Control de Recursos Tecnológicos (ESPECÍFICO)
# ---------------------------------------------------------
elif modulo_seleccionado == "2. Préstamo de Recursos":
    st.header("💻 Módulo 2: Préstamo y Control de Recursos Tecnológicos")
    st.write("Control y trazabilidad de los equipos tecnológicos del campus con registro oficial de solicitante.")

    col_res1, col_res2 = st.columns(2)

    with col_res1:
        st.markdown("<div style='background-color: #33373E; padding: 20px; border-radius: 10px;'>", unsafe_allow_html=True)
        st.subheader("Datos del Solicitante y Equipo")
        
        id_recurso_input = st.text_input("ID del Recurso Tecnológico", placeholder="Ej: REC-001")
        doc_solicitante = st.text_input("Número de Documento / PIN de Asistencia", placeholder="Ingrese su número de cédula o PIN")
        nombre_solicitante = st.text_input("Nombres", placeholder="Ingrese sus nombres")
        apellido_solicitante = st.text_input("Apellidos", placeholder="Ingrese sus apellidos")
        
        prestar_btn = st.button("Validar y Registrar Préstamo")
        st.markdown("</div>", unsafe_allow_html=True)

    with col_res2:
        st.markdown("<div style='background-color: #33373E; padding: 20px; border-radius: 10px;'>", unsafe_allow_html=True)
        st.subheader("Estado de la Solicitud")

        if prestar_btn:
            if id_recurso_input.strip() and doc_solicitante.strip() and nombre_solicitante.strip() and apellido_solicitante.strip():
                val_rec, msg_rec = validar_recurso_para_prestamo(id_recurso_input.strip())
                if val_rec:
                    st.success(f"📦 **Préstamo Aprobado:** {msg_rec}")
                    st.markdown(f"- **Solicitante:** {nombre_solicitante} {apellido_solicitante}")
                    st.markdown(f"- **Documento / PIN:** {doc_solicitante}")
                else:
                    st.error(f"❌ **Préstamo Denegado:** {msg_rec}")
            else:
                st.warning("⚠️ **Atención:** Debe completar todos los campos (ID del recurso, Documento/PIN, Nombre y Apellido) para procesar el préstamo.")
        else:
            st.info("ℹ️ Complete los datos del solicitante y el ID del recurso tecnológico para verificar las reglas de disponibilidad en el inventario.")
        st.markdown("</div>", unsafe_allow_html=True)

# ---------------------------------------------------------
# MÓDULO 3: Triaje de Incidencias con IA
# ---------------------------------------------------------
elif modulo_seleccionado == "3. Triaje de Incidencias":
    st.header("🤖 Módulo 3: Triaje Inteligente de Incidencias con IA")
    st.markdown("<span style='background-color: #6B5BFF; color: white; padding: 4px 10px; border-radius: 6px; font-size: 12px; font-weight: bold;'>[Ref-Core] Asistente Operativo IA</span>", unsafe_allow_html=True)
    st.write("Clasificación, priorización y enrutamiento automatizado de solicitudes mediante el modelo de Inteligencia Artificial autorizado.")

    incidencia_usuario = st.text_area("Describa la incidencia reportada en el campus:", placeholder="Ej: El proyector del auditorio presenta fallas de conexión HDMI y hay evento a las 2 PM...")

    if st.button("Analizar Incidencia con IA"):
        if incidencia_usuario.strip():
            with st.spinner("Procesando análisis dinámico con la API de Gemini..."):
                respuesta_IA = procesar_triaje_con_ia(incidencia_usuario)
                
                st.markdown("---")
                st.subheader("📋 Resultado del Análisis Operativo")
                
                if "error" in respuesta_IA:
                    st.error(respuesta_IA["error"])
                else:
                    st.markdown(f"<div style='background-color: #33373E; padding: 20px; border-radius: 10px; border-left: 5px solid #00D2D3;'>", unsafe_allow_html=True)
                    st.markdown(f"**Respuesta del Sistema de IA:**\n\n{respuesta_IA.get('resultado_ia', 'Sin respuesta')}")
                    st.markdown("</div>", unsafe_allow_html=True)
        else:
            st.warning("⚠️ Por favor, ingrese una descripción antes de ejecutar el análisis.")

# Pie de página técnico oficial requerido por la hackatón
st.markdown("---")
st.markdown("<p style='text-align: center; color: #8c929d; font-size: 12px;'>Campuslands Academic QA & Telemetry Spec (v2.6) • Protocolo PSA-9 • Build-Ref: CL-884-X</p>", unsafe_allow_html=True)