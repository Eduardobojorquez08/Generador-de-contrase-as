from generador import crear_contraseña, pedir_longitud
from verificador import verificar_contraseña

print("Bienvenido al Generador de Contraseñas")
print("¿Que es lo que estas buscando?")
print("1. Crear una Contraseña aleatoria")
print("2. Verificar la seguridad de tu Contraseña")
print("3. Salir")

while True:
    opcion = input("Elige una opcion(1 , 2 , 3):").strip()

    if opcion == "1":
       longitud = pedir_longitud()
       contraseña_creada = crear_contraseña(longitud)
       print(f"Tu contraseña es: {contraseña_creada}")
       
    elif opcion == "2":
         contraseña_usuario = input("Ingresa tu contraseña para verificar su seguridad: ")
         verificar_contraseña(contraseña_usuario)
         
    elif opcion == "3":
        print("Saliste del Generador de Contraseñas!")
        exit()
    else:
        print("Opcion no valida")