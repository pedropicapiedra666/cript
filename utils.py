def pedir_clave():
    return input("Ingrese su clave privada: ").strip()

def pedir_modo():
    while True:
        modo = input("¿Desea (E)ncriptar o (D)esencriptar?: ").strip().lower()
        if modo in ['e', 'd']:
            return modo
        print("Opción inválida. Use 'E' para encriptar o 'D' para desencriptar.")
