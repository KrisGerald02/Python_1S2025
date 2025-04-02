#Create Enviroment
#Ctrl + Shift + P
#Python: Create Enviroment
#.venv
#Select 3.13.2 version
def solicitar_lista():
    """Solicita al usuario que ingrese una lista de cadenas separadas por comas."""
    entrada = input("Ingrese las cadenas separadas por comas: ")
    return [cadena.strip() for cadena in entrada.split(",")]

def concatenar_cadenas(lista):
    return " ".join(lista)

def longitud_cadenas(lista):
    return [len(cadena) for cadena in lista]

def convertir_cadenas(lista):
    return [cadena.upper() if len(cadena) % 2 == 0 else cadena.lower() for cadena in lista]

def buscar_subcadena(lista, subcadena):
    """Busca una subcadena en cada elemento de la lista e indica la posición donde se encuentra."""
    resultados = [(i, cadena) for i, cadena in enumerate(lista) if subcadena in cadena]
    
    if resultados:
        return "\n".join([f"Posición {i}: '{cadena}'" for i, cadena in resultados])
    else:
        return f"La subcadena '{subcadena}' no se encontró en ninguna cadena."



def reemplazar_caracter(lista, viejo, nuevo):
    return [cadena.replace(viejo, nuevo) for cadena in lista]

def eliminar_espacios(lista):
    return [cadena.strip() for cadena in lista]

def dividir_cadenas(lista, delimitador):
    return [cadena.split(delimitador) for cadena in lista]

def ordenar_cadenas(lista):
    return sorted(lista)

def eliminar_vacias(lista):
    return [cadena for cadena in lista if cadena]

def contar_caracter(lista, caracter):
    return [cadena.count(caracter) for cadena in lista]

def menu():
    print("\nMenú de opciones:")
    print("1. Concatenar cadenas")
    print("2. Calcular longitud de cadenas")
    print("3. Convertir cadenas según longitud")
    print("4. Buscar subcadena en cadenas")
    print("5. Reemplazar caracteres en cadenas")
    print("6. Eliminar espacios en cadenas")
    print("7. Dividir cadenas por delimitador")
    print("8. Ordenar cadenas alfabéticamente")
    print("9. Eliminar cadenas vacías")
    print("10. Contar caracteres en cadenas")
    print("0. Salir")
    opcion = input("Seleccione una opción: ")
    return opcion

def ejecutar_opcion(opcion):
    if opcion == "0":
        print("Saliendo...")
        return False

    lista = solicitar_lista()  # Se solicita la lista de cadenas

    if opcion == "1":
        print("Cadenas concatenadas:", concatenar_cadenas(lista))
    elif opcion == "2":
        print("Longitud de cada cadena:", longitud_cadenas(lista))
    elif opcion == "3":
        print("Cadenas convertidas según longitud:", convertir_cadenas(lista))
    elif opcion == "4":
        subcadena = input("Ingrese la subcadena a buscar: ")
        print("Subcadena encontrada en cada cadena:", buscar_subcadena(lista, subcadena))
    elif opcion == "5":
        viejo = input("Ingrese el carácter a reemplazar: ")
        nuevo = input("Ingrese el nuevo carácter: ")
        print("Cadenas modificadas:", reemplazar_caracter(lista, viejo, nuevo))
    elif opcion == "6":
        print("Cadenas sin espacios:", eliminar_espacios(lista))
    elif opcion == "7":
        delimitador = input("Ingrese el delimitador: ")
        print("Cadenas divididas:", dividir_cadenas(lista, delimitador))
    elif opcion == "8":
        print("Cadenas ordenadas:", ordenar_cadenas(lista))
    elif opcion == "9":
        print("Cadenas sin vacías:", eliminar_vacias(lista))
    elif opcion == "10":
        caracter = input("Ingrese el carácter a contar: ")
        print("Cantidad de veces que aparece el carácter:", contar_caracter(lista, caracter))
    else:
        print(" Opcion no valida. Intente de nuevo.")
    
    return True

if __name__ == "__main__":
    while True:
        opcion = menu()
        if not ejecutar_opcion(opcion):
            break
