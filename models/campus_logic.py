import json
from pathlib import Path

RUTA_DATOS = (
    Path(__file__).resolve().parent.parent
    / "data"
    / "datos_campus.json"
)

def cargar_datos():
    if not RUTA_DATOS.exists():
        raise FileNotFoundError(
            f"No se encontró el archivo: {RUTA_DATOS}"
        )

    try:
        with open(RUTA_DATOS, "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)

    except json.JSONDecodeError as error:
        raise ValueError(
            "El archivo JSON tiene un formato incorrecto."
        ) from error

    
    if not isinstance(datos, dict):
        raise ValueError(
            "La estructura principal del JSON debe ser un objeto."
        )

    for seccion in ("espacios", "recursos", "incidencias"):
        if not isinstance(datos.get(seccion), list):
            raise ValueError(
                f"La sección '{seccion}' debe ser una lista."
            )

    return datos