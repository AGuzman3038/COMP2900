def invertir_arreglo(arreglo):
    longitud = len(arreglo)
    for i in range(longitud // 2):
        # Intercambia los elementos del inicio y del final del arreglo
        arreglo[i], arreglo[longitud - 1 - i] = arreglo[longitud - 1 - i], arreglo[i]

# Ejemplo de uso:
def main():
    arreglo_numeros = [1, 2, 3, 4, 5]
    print("Arreglo original:", arreglo_numeros)
    invertir_arreglo(arreglo_numeros)
    print("Arreglo invertido:", arreglo_numeros)

if __name__ == "__main__":
    main()
