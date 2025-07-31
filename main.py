import hashlib
import random
from datetime import datetime

# =====================
# CARGAR PALABRAS
# =====================
def cargar_palabras(archivo="palabras.txt"):
    with open(archivo, "r", encoding="utf-8") as f:
        return [line.strip() for line in f.readlines()]

# =====================
# GENERAR MAPEOS
# =====================
def generar_diccionario(clave_privada, fecha=None):
    if fecha is None:
        fecha = datetime.now().strftime("%Y-%m-%d")
    
    caracteres = "abcdefghijklmnopqrstuvwxyz0123456789 "
    semilla = hashlib.sha256((clave_privada + fecha).encode()).hexdigest()
    random.seed(semilla)
    
    palabras = cargar_palabras()
    random.shuffle(palabras)
    
    # Crear mapeo (incluye espacio)
    diccionario = {car: palabras[i] for i, car in enumerate(caracteres)}
    return diccionario

# =====================
# CIFRADO
# =====================
def cifrar(mensaje, clave_privada):
    diccionario = generar_diccionario(clave_privada)
    mensaje = mensaje.lower()
    return " ".join(diccionario[char] if char in diccionario else char for char in mensaje)

# =====================
# DESCIFRADO
# =====================
def descifrar(mensaje, clave_privada, fecha=None):
    diccionario = generar_diccionario(clave_privada, fecha)
    inverso = {v: k for k, v in diccionario.items()}
    palabras = mensaje.split()
    return "".join(inverso.get(palabra, palabra) for palabra in palabras)

# =====================
# PROBAR
# =====================
if __name__ == "__main__":
    clave = input("🔑 Ingrese su clave privada: ")
    opcion = input("¿Desea (C)ifrar o (D)escifrar? ").lower()

    if opcion == "c":
        mensaje = input("Ingrese el mensaje a cifrar: ")
        print("🔒 Mensaje cifrado:\n", cifrar(mensaje, clave))
    elif opcion == "d":
        mensaje = input("Ingrese el mensaje a descifrar: ")
        fecha = input("Ingrese la fecha del mensaje (YYYY-MM-DD) o Enter para hoy: ")
        fecha = fecha if fecha else None
        print("🔑 Mensaje descifrado:\n", descifrar(mensaje, clave, fecha))
