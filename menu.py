def concatenar_cadenas(lista):
    return " ".join(lista)

def longitud_cadenas(lista):
    return [len(cadena) for cadena in lista]

def convertir_cadenas(lista):
    return [cadena.upper() if len(cadena) % 2 == 0 else cadena.lower() for cadena in lista]

def buscar_subcadena(lista, subcadena):
    return [subcadena in cadena for cadena in lista]

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
    print("\nMenu de opciones:")
    print("1. Concatenar cadenas")
    print("2. Calcular longitud de cadenas")
    print("3. Convertir cadenas segun longitud")
    print("4. Buscar subcadena en cadenas")
    print("5. Reemplazar caracteres en cadenas")
    print("6. Eliminar espacios en cadenas")
    print("7. Dividir cadenas por delimitador")
    print("8. Ordenar cadenas alfabeticamente")
    print("9. Eliminar cadenas vacias")
    print("10. Contar caracteres en cadenas")
    print("0. Salir")
    return input("Seleccione una opcion: ")

def ejecutar_opcion(opcion, lista):
    if opcion == "1":
        print("Ejercicio 1: Concatenar todas las cadenas en una sola cadena, separadas por un espacio.")
        print(concatenar_cadenas(lista))
    elif opcion == "2":
        print("Ejercicio 2: Calcular la longitud de cada cadena y almacenarla en una nueva lista.")
        print(longitud_cadenas(lista))
    elif opcion == "3":
        print("Ejercicio 3: Convertir cadenas a mayusculas si son de longitud par, minusculas si son impares.")
        print(convertir_cadenas(lista))
    elif opcion == "4":
        print("Ejercicio 4: Buscar si una subcadena esta presente en cada cadena de la lista.")
        subcadena = input("Ingrese la subcadena a buscar: ")
        print(buscar_subcadena(lista, subcadena))
    elif opcion == "5":
        print("Ejercicio 5: Reemplazar un caracter especifico con otro en cada cadena.")
        viejo = input("Ingrese el caracter a reemplazar: ")
        nuevo = input("Ingrese el nuevo caracter: ")
        print(reemplazar_caracter(lista, viejo, nuevo))
    elif opcion == "6":
        print("Ejercicio 6: Eliminar espacios en blanco al inicio y final de cada cadena.")
        print(eliminar_espacios(lista))
    elif opcion == "7":
        print("Ejercicio 7: Dividir cada cadena en subcadenas utilizando un delimitador especifico.")
        delimitador = input("Ingrese el delimitador: ")
        print(dividir_cadenas(lista, delimitador))
    elif opcion == "8":
        print("Ejercicio 8: Ordenar la lista alfabeticamente en orden ascendente.")
        print(ordenar_cadenas(lista))
    elif opcion == "9":
        print("Ejercicio 9: Eliminar cadenas vacias de la lista.")
        print(eliminar_vacias(lista))
    elif opcion == "10":
        print("Ejercicio 10: Contar cuantas veces aparece un caracter especifico en cada cadena.")
        caracter = input("Ingrese el caracter a contar: ")
        print(contar_caracter(lista, caracter))
    elif opcion == "0":
        print("Saliendo...")
        return False
    else:
        print("Opcion no valida.")
    return True

if __name__ == "__main__":
    lista_ejemplo = ["Hola", "Mundo", "Python", "", "Estructuras de datos"]
    while True:
        opcion = menu()
        if not ejecutar_opcion(opcion, lista_ejemplo):
            break
