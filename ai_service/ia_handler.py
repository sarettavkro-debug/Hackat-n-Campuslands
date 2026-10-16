import os
from google import genai
from dotenv import load_dotenv

# Carga las variables de entorno de forma segura (.env)
load_dotenv()

def procesar_triaje_con_ia(descripcion_incidencia):
    """
    Envía la incidencia real a la API de Gemini para un triaje dinámico,
    cumpliendo con el flujo operativo del campus.
    """
    api_key = os.getenv("GEMINI_API_KEY")
    
    # Validación por seguridad si falta la clave
    if not api_key:
        return {
            "error": "API Key no configurada en las variables de entorno.",
            "categoria": "Error de Sistema",
            "prioridad": "N/A"
        }

    try:
        # Inicialización del cliente oficial de Google GenAI
        client = genai.Client(api_key=api_key)
        
        # Prompt estructurado para forzar una respuesta clara y útil para el campus
        prompt = f"""
        [Ref-Core] Actúa como el motor de Inteligencia Artificial del Sistema Central 
        de Gestión Operativa de Campuslands. Analiza la siguiente incidencia reportada:
        
        "{descripcion_incidencia}"
        
        Devuelve la respuesta estrictamente en este formato:
        - Categoría: (Elige entre: Espacios, Recursos Tecnológicos o Incidencia General)
        - Prioridad: (Elige entre: Alta, Media o Baja)
        - Recomendación Operativa: (Una breve instrucción de acción para el equipo)
        """

        # Llamada al modelo autorizado
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=prompt,
        )

        return {
            "resultado_ia": response.text,
            "estado": "Exitoso"
        }
        
    except Exception as e:
        # Manejo de excepciones para evitar que la aplicación falle frente al jurado
        return {
            "error": f"Error de conexión con la IA: {str(e)}",
            "categoria": "Indeterminado",
            "prioridad": "Media"
        }