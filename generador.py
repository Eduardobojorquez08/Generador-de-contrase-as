import random
import string

def crear_contraseña(longitud):
    simbolos_permitidos = string.ascii_uppercase + string.ascii_lowercase + string.digits + "!¡@&$*()"
    contraseña = "".join(random.choices(simbolos_permitidos, k=longitud))
    return contraseña


def pedir_longitud():
    while True:
        texto = input("¿Que tan larga deseas que sea la contraseña?").strip()

        if texto.isdigit():
            return int(texto)
        else:
            print("Error")
