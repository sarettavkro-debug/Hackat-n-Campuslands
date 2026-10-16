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

def listar_espacios():
    
    datos = cargar_datos
    return datos["espacios"]

def buscar_espacio(id_espacio):
    
    for espacio in listar_espacios():
        if espacio.get("id") == id_espacio:
            return espacio

    return None

def validar_capacidad(id_espacio, cantidad_personas):

    if (
        isinstance(cantidad_personas, bool)
        or not isinstance(cantidad_personas, int)
        or cantidad_personas <= 0
    ):
        return False, "La cantidad de personas debe ser un entero positivo."

    espacio = buscar_espacio(id_espacio)

    if espacio is None:
        return False, "El espacio no existe."

    capacidad = espacio.get("capacidad")

    if (
        isinstance(capacidad, bool)
        or not isinstance(capacidad, int)
        or capacidad <= 0
    ):
        return False, "El espacio tiene una capacidad inválida."

    if cantidad_personas > capacidad:
        return (
            False,
            f"El espacio admite máximo {capacidad} personas."
        )

    return True, "La capacidad es suficiente."

def validar_disponibilidad_espacio(id_espacio):

    espacio = buscar_espacio(id_espacio)

    if espacio is None:
        return False, "El espacio no existe."

    if espacio.get("estado") != "disponible":
        return False, "El espacio no está disponible."

    return True, "El espacio está disponible."

def validar_recurso_para_prestamo(id_recurso):

    datos = cargar_datos()

    for recurso in datos["recursos"]:
        if recurso.get("id") == id_recurso:

            if recurso.get("estado") != "operativo":
                return False, "El recurso no está operativo."

            if recurso.get("disponibilidad") != "disponible":
                return False, "El recurso ya está prestado o no disponible."

            return True, "El recurso puede prestarse."

    return False, "El recurso no existe."

def actualizar_estado_espacio(id_espacio, nuevo_estado):

    estados_validos = {
        "disponible",
        "ocupado",
        "inhabilitado"
    }

    if nuevo_estado not in estados_validos:
        raise ValueError("El estado indicado no es válido.")

    datos = cargar_datos()

    for espacio in datos["espacios"]:
        if espacio.get("id") == id_espacio:
            espacio["estado"] = nuevo_estado
            guardar_datos(datos)
            return True

    return False