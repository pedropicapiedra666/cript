import random
import datetime

CARACTERES = "abcdefghijklmnopqrstuvwxyz0123456789"

def cargar_palabras(ruta: str):
    with open(ruta, "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]

def generar_diccionario(clave_privada: str, fecha: str, palabras: list):
    random.seed(clave_privada + fecha)
    palabras_unicas = palabras.copy()
    random.shuffle(palabras_unicas)

    if len(palabras_unicas) < len(CARACTERES):
        raise ValueError("No hay suficientes palabras en el banco de palabras")

    return {c: palabras_unicas[i] for i, c in enumerate(CARACTERES)}

def generar_diccionario_inverso(diccionario):
    return {v: k for k, v in diccionario.items()}

def obtener_fecha_actual():
    return datetime.date.today().strftime("%Y%m%d")
