import hashlib
import random
from datetime import datetime
from fastapi import FastAPI
from pydantic import BaseModel

# =====================
# CARGAR PALABRAS
# =====================
def cargar_palabras(archivo="palabras.txt"):
    with open(archivo, "r", encoding="utf-8") as f:
        return [line.strip() for line in f.readlines()]

# =====================
# GENERAR DICCIONARIO
# =====================
def generar_diccionario(clave_privada, fecha=None):
    if fecha is None:
        fecha = datetime.now().strftime("%Y-%m-%d")

    caracteres = "abcdefghijklmnopqrstuvwxyz0123456789 .,!?¡¿"
    semilla = hashlib.sha256((clave_privada + fecha).encode()).hexdigest()
    random.seed(semilla)
    palabras = cargar_palabras()
    random.shuffle(palabras)

    return {car: palabras[i] for i, car in enumerate(caracteres)}

# =====================
# CIFRAR
# =====================
def cifrar(mensaje, clave_privada):
    diccionario = generar_diccionario(clave_privada)
    mensaje = mensaje.lower()
    return " ".join(diccionario[char] if char in diccionario else char for char in mensaje)

# =====================
# DESCIFRAR
# =====================
def descifrar(mensaje, clave_privada, fecha=None):
    diccionario = generar_diccionario(clave_privada, fecha)
    inverso = {v: k for k, v in diccionario.items()}
    palabras = mensaje.split()
    return "".join(inverso.get(p, p) for p in palabras)

# =====================
# API
# =====================
app = FastAPI()

class CifrarRequest(BaseModel):
    mensaje: str
    clave: str

class DescifrarRequest(BaseModel):
    mensaje: str
    clave: str
    fecha: str | None = None  # Opcional

@app.post("/cifrar")
def endpoint_cifrar(data: CifrarRequest):
    return {"mensaje_cifrado": cifrar(data.mensaje, data.clave)}

@app.post("/descifrar")
def endpoint_descifrar(data: DescifrarRequest):
    return {"mensaje_descifrado": descifrar(data.mensaje, data.clave, data.fecha)}

@app.get("/")
def root():
    return {"message": "API de cifrado funcionando en Vercel"}
