# 🏫 Sistema Central de Gestión Operativa - El Campus Bajo Presión

> **Solución Tecnológica de Gestión Integral para Campuslands**  
> Desarrollo presentado en el marco de la Hackatón para optimizar la administración de espacios físicos, el control de préstamos de inventario tecnológico y la categorización automatizada de incidencias operativas mediante Inteligencia Artificial.

---

## 👥 Equipo de Trabajo y Definición de Roles

| Rol | Integrante | Responsabilidades Principales |
| :--- | :--- | :--- |
| **Persona 1: Backend & Data** | Integrante 1 | Diseño del modelo de datos (`datos_campus.json`), reglas de negocio y funciones de validación lógica (`campus_logic.py`). |
| **Persona 2: AI Engineer** | Integrante 2 | Integración del modelo de IA, desarrollo de endpoints de procesamiento y algoritmos para el triaje de incidencias (`ai_service/`). |
| **Persona 3: Frontend & Git Manager** | Persona 3 | Diseño de la interfaz interactiva en Streamlit (`app.py`), gestión de ramas/commits en Git y documentación central del proyecto (`README.md`). |

---

## 🚀 Arquitectura del Proyecto y Estructura de Directorios

El proyecto implementa una arquitectura modular que separa estrictamente la capa de presentación (UI), la capa de procesamiento lógico/negocio y la capa de persistencia de datos:

```text
Hackat-n-Campuslands/
│
├── app.py                  # Interfaz gráfica principal desarrollada en Streamlit (Persona 3)
├── requirements.txt        # Definición de dependencias y versiones de paquetes Python
├── .gitignore              # Configuración de exclusión para Git (entorno virtual, temporales)
├── README.md               # Documentación general y guía técnica del proyecto
│
├── data/                   # Capa de almacenamiento y datos persistentes
│   └── datos_campus.json   # Base de datos centralizada en formato JSON (Persona 1)
│
├── models/                 # Capa de lógica de negocio y reglas del sistema
│   ├── __init__.py         # Inicializador del módulo Python
│   └── campus_logic.py     # Funciones de validación de aforo, estados y lectura JSON (Persona 1)
│
└── ai_service/             # Capa de Inteligencia Artificial y triaje
    ├── __init__.py         # Inicializador del módulo Python
    └── classifier.py       # Lógica de clasificación y priorización de reportes (Persona 2)

## 📌 Módulos del Sistema

### 🏢 Módulo 1: Disponibilidad y Reserva de Espacios
* **Descripción:** Gestión y control en tiempo real de aulas, laboratorios y cubículos del campus.
* **Lógica de Negocio:**
  * Lectura dinámica de espacios disponibles desde la base de datos centralizada (`datos_campus.json`).
  * Validación estricta de aforos máximos permitidos por cada lugar.
  * Prevención de sobrecupos y solapamientos de horarios.
* **Interfaz de Usuario:**
  * Selector dinámico de aulas y entrada numérica para la cantidad de asistentes.
  * Retroalimentación visual inmediata con alertas de color según disponibilidad (`st.success`, `st.error`).

### 📦 Módulo 2: Control y Préstamo de Recursos Tecnológicos
* **Descripción:** Control de inventario y trazabilidad de entrega de equipos tecnológicos (proyectores, laptops, tablets, cables).
* **Lógica de Negocio:**
  * Verificación del estado y disponibilidad previa del equipo solicitado.
  * Registro y trazabilidad de préstamos asociados al documento del usuario solicitante.
* **Interfaz de Usuario:**
  * Menú desplegable con el catálogo de equipos del campus.
  * Formulario de captura de datos del solicitante con confirmación inmediata del préstamo.

### 🤖 Módulo 3: Triaje Inteligente de Incidencias con IA
* **Descripción:** Categorización y priorización automatizada de reportes e incidentes operativos mediante IA.
* **Lógica de Negocio:**
  * Procesamiento de lenguaje natural sobre la descripción del problema ingresado por el usuario.
  * Clasificación por categorías operativas (Mantenimiento Técnico, Infraestructura, Redes/TI).
  * Asignación automática del nivel de prioridad (Alta, Media, Baja) para optimizar tiempos de respuesta.
* **Interfaz de Usuario:**
  * Área de texto enriquecida para descripción detallada de fallas.
  * Indicador de procesamiento en vivo y métrica destacada de la prioridad asignada.