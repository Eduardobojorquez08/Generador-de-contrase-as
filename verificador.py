def verificar_contraseña(contraseña):
    tiene_mayuscula = any(c.isupper() for c in contraseña)
    tiene_minuscula = any(c.islower() for c in contraseña)
    tiene_numero = any(c.isdigit() for c in contraseña)
    tiene_longitud = len(contraseña) >= 8

    if tiene_mayuscula and tiene_minuscula and tiene_numero and tiene_longitud:
        return "Tu contraseña si es segura"
    else:
        sugerencias = "Te falta: "
        if not tiene_mayuscula:
            sugerencias += "Mayúsculas, "
        if not tiene_minuscula:
            sugerencias += "Minúsculas, "
        if not tiene_numero:
            sugerencias += "Números, "
        if not tiene_longitud:
            sugerencias += "Más de 8 caracteres, "
        return sugerencias