# 🏫 Sistema Central de Gestión Operativa - El Campus Bajo Presión

> **Solución Tecnológica de Gestión Integral para Campuslands**
> Desarrollo presentado en el marco de la Hackatón para optimizar la administración de espacios físicos, el control de préstamos de inventario tecnológico y la categorización automatizada de incidencias operativas mediante Inteligencia Artificial.

---

## 👥 Equipo de Trabajo y Definición de Roles

| Rol | Integrante | Responsabilidades Principales |
| :--- | :--- | :--- |
| **Persona 1: Backend & Data** | Integrante 1 | Diseño del modelo de datos (`datos_campus.json`), reglas de negocio y funciones de validación lógica (`campus_logic.py`). |
| **Persona 2: AI Engineer** | Integrante 2 | Integración del modelo de IA, desarrollo de endpoints de procesamiento y algoritmos para el triaje de incidencias (`ai_service/`). |
| **Persona 3: Frontend & Git Manager** | Integrante 3 | Diseño de la interfaz interactiva en Streamlit (`app.py`), gestión de ramas/commits en Git y documentación central del proyecto (`README.md`). |

---

## 🚀 Arquitectura del Proyecto y Estructura de Directorios

```text
Hackat-n-Campuslands/
│
├── .env                  # Variables de entorno y credenciales de configuración
├── requeriments.txt      # Dependencias del proyecto Python
├── app.py                # Aplicación principal de la interfaz web en Streamlit
├── datos_campus.json     # Base de datos local (espacios, aforos y recursos)
├── campus_logic.py       # Lógica de negocio y validaciones operativas
├── ai_service/           # Servicio de IA para el triaje de incidencias
└── README.md             # Documentación oficial del proyecto
```

---

## 📌 Módulos del Sistema

### 🏢 Módulo 1: Disponibilidad y Reserva de Espacios

**Descripción:** Gestión y control en tiempo real de aulas, laboratorios y cubículos del campus.

**Lógica de Negocio:**

* Lectura dinámica de espacios disponibles desde la base de datos centralizada (`datos_campus.json`).
* Validación estricta de aforos máximos permitidos por cada lugar.
* Prevención de sobrecupos y solapamientos de horarios.

**Interfaz de Usuario:**

* Selector dinámico de aulas y entrada numérica para la cantidad de asistentes.
* Retroalimentación visual inmediata con alertas de color según disponibilidad (`st.success`, `st.error`).

---

### 📦 Módulo 2: Control y Préstamo de Recursos Tecnológicos

**Descripción:** Control de inventario y trazabilidad de entrega de equipos tecnológicos (proyectores, laptops, tablets, cables).

**Lógica de Negocio:**

* Verificación del estado y disponibilidad previa del equipo solicitado.
* Registro y trazabilidad de préstamos asociados al documento del usuario solicitante.

**Interfaz de Usuario:**

* Menú desplegable con el catálogo de equipos del campus.
* Formulario de captura de datos del solicitante con confirmación inmediata del préstamo.

---

### 🤖 Módulo 3: Triaje Inteligente de Incidencias con IA

**Descripción:** Categorización y priorización automatizada de reportes e incidentes operativos mediante IA.

**Lógica de Negocio:**

* Procesamiento de lenguaje natural sobre la descripción del problema ingresado por el usuario.
* Clasificación por categorías operativas (Mantenimiento Técnico, Infraestructura, Redes/TI).
* Asignación automática del nivel de prioridad (Alta, Media, Baja) para optimizar tiempos de respuesta.

**Interfaz de Usuario:**

* Área de texto enriquecida para descripción detallada de fallas.
* Indicador de procesamiento en vivo y métrica destacada de la prioridad asignada.

---

## ⚙️ Guía Paso a Paso de Instalación y Ejecución Local

### Prerrequisitos

Asegúrate de contar con **Python 3.10 o superior** instalado en tu sistema operativo y acceso a una terminal de comandos.

### 1. Clonar el Repositorio

```bash
git clone <URL_DE_TU_REPOSITORIO>
cd Hackat-n-Campuslands
```

### 2. Crear y Activar el Entorno Virtual

Es altamente recomendable aislar las dependencias dentro de un entorno virtual (`venv`).

**En Linux / macOS:**

```bash
python3 -m venv venv
source venv/bin/activate
```

**En Windows (PowerShell):**

```powershell
python -m venv venv
.\venv\Scripts\Activate
```

### 3. Instalar Dependencias

Instala todos los paquetes requeridos especificados en el archivo de requerimientos:

```bash
pip install -r requeriments.txt
```

### 4. Ejecutar la Aplicación

Inicia el servidor local de Streamlit ejecutando:

```bash
streamlit run app.py
```

La interfaz web se desplegará automáticamente en tu navegador predeterminado en `http://localhost:8501`.

---

## 🔄 Flujo de Trabajo en Git y Colaboración

Para mantener la estabilidad del proyecto durante la hackatón, se aplican las siguientes buenas prácticas:

### 1. Sincronización constante

```bash
git pull origin main
```

### 2. Commits atómicos y descriptivos

```bash
git add .
git commit -m "docs: corregir estructura del README para separar la arquitectura"
```

### 3. Publicación de cambios

```bash
git push origin main
```