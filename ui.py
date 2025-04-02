def solicitar_lista():
    """Solicita al usuario que ingrese una lista de cadenas separadas por comas."""
    entrada = input("Ingrese las cadenas separadas por comas: ")
    return [cadena.strip() for cadena in entrada.split(",")]

def invertir_cadenas(lista):
    return [cadena[::-1] for cadena in lista]

def eliminar_vocales(lista):
    vocales = "aeiouAEIOU"
    return [''.join([letra for letra in cadena if letra not in vocales]) for cadena in lista]

def reemplazar_palabra(lista, vieja_palabra, nueva_palabra):
    return [cadena.replace(vieja_palabra, nueva_palabra) for cadena in lista]

def contar_palabras(lista):
    return [len(cadena.split()) for cadena in lista]

def invertir_caso(lista):
    return [cadena.swapcase() for cadena in lista]

def eliminar_cadenas_cortas(lista):
    return [cadena for cadena in lista if len(cadena) >= 3]

def encontrar_extremos(lista):
    mas_larga = max(lista, key=len)
    mas_corta = min(lista, key=len)
    return mas_larga, mas_corta

def menu():
    print("\nMenú de opciones:")
    print("1. Invertir las cadenas")
    print("2. Eliminar todas las vocales de las cadenas")
    print("3. Reemplazar una palabra por otra")
    print("4. Contar la cantidad de palabras en cada cadena")
    print("5. Cambiar el caso de todas las letras")
    print("6. Eliminar las cadenas con menos de 3 caracteres")
    print("7. Encontrar la cadena más larga y la más corta")
    print("0. Salir")
    opcion = input("Seleccione una opción: ")
    return opcion

def ejecutar_opcion(opcion):
    if opcion == "0":
        print("Saliendo...")
        return False

    lista = solicitar_lista()  # Se solicita la lista de cadenas

    if opcion == "1":
        print("Cadenas invertidas:", invertir_cadenas(lista))
    elif opcion == "2":
        print("Cadenas sin vocales:", eliminar_vocales(lista))
    elif opcion == "3":
        vieja_palabra = input("Ingrese la palabra a reemplazar: ")
        nueva_palabra = input("Ingrese la nueva palabra: ")
        print("Cadenas modificadas:", reemplazar_palabra(lista, vieja_palabra, nueva_palabra))
    elif opcion == "4":
        print("Cantidad de palabras en cada cadena:", contar_palabras(lista))
    elif opcion == "5":
        print("Cadenas con el caso invertido:", invertir_caso(lista))
    elif opcion == "6":
        print("Cadenas eliminadas (menos de 3 caracteres):", eliminar_cadenas_cortas(lista))
    elif opcion == "7":
        mas_larga, mas_corta = encontrar_extremos(lista)
        print(f"Cadena más larga: {mas_larga}")
        print(f"Cadena más corta: {mas_corta}")
    else:
        print("Opción no válida. Intente de nuevo.")
    
    return True

if __name__ == "__main__":
    while True:
        opcion = menu()
        if not ejecutar_opcion(opcion):
            break
