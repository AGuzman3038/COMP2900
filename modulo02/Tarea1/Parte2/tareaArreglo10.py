def rotar_arreglo_derecha(arreglo):
    if not arreglo:  # Verifica si el arreglo está vacío
        return arreglo

    ultimo_elemento = arreglo[-1]
    for i in range(len(arreglo) - 1, 0, -1):
        arreglo[i] = arreglo[i - 1]
    arreglo[0] = ultimo_elemento

# Ejemplo de uso:
def main():
    arreglo_numeros = [1, 2, 3, 4, 5]
    print("Arreglo original:", arreglo_numeros)
    rotar_arreglo_derecha(arreglo_numeros)
    print("Arreglo con los elementos rotados a la derecha:", arreglo_numeros)

if __name__ == "__main__":
    main()
