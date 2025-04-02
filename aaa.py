def modificar_cadena(cadena):
    # Definir las vocales
    vocales = "aeiouAEIOU"
    
    # Comprobar si la cadena no está vacía
    if len(cadena) > 0:
        # Hacer que toda la cadena sea en minúsculas
        cadena = cadena.lower()

        # Si empieza con una vocal
        if cadena[0] in vocales:
            # Convertir la última letra a mayúscula
            return cadena[:-1] + cadena[-1].upper()
        else:
            # Si empieza con consonante, convertir el primer carácter a mayúscula
            return cadena[0].upper() + cadena[1:]
    else:
        # Si la cadena está vacía, no hacer nada
        return cadena

# Solicitar la entrada al usuario
cadena = input("Ingresa una cadena: ")

# Modificar la cadena según la condición
cadena_modificada = modificar_cadena(cadena)

# Mostrar el resultado
print("Cadena modificada:", cadena_modificada)
