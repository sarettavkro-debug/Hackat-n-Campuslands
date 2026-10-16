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

def guardar_datos(datos):
    
    if not isinstance(datos, dict):
        raise ValueError("Los datos deben estar en un diccionario")

    for seccion in ("espacios", "recursos", "incidencias"):
        if not isinstance(datos.get(seccion), list):
            raise ValueError(
                f"La sección '{seccion}' debe ser una lista."
            )

    ruta_temporal = RUTA_DATOS.with_suffix(".tmp")

    try:
        with open(ruta_temporal, "w", encoding="utf-8") as archivo:
            json.dump(
                datos,
                archivo,
                ensure_ascii=False,
                indent=4
            )

        ruta_temporal.replace(datos)

    finally:
        if ruta_temporal.exists():
            ruta_temporal.unlink()

