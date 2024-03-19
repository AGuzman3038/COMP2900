def es_numero_entero(cadena):

    try:
        int(cadena)
        return True
    except ValueError:
        return False


entrada_usuario = input("Ingresa un número entero: ")

if es_numero_entero(entrada_usuario):
    print(f"{entrada_usuario} es un número entero.")
else:
    print(f"{entrada_usuario} no es un número entero.")
