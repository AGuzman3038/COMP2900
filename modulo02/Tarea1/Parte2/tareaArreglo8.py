def ordenar_arreglo(arreglo):
    n = len(arreglo)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arreglo[j] > arreglo[j + 1]:
                arreglo[j], arreglo[j + 1] = arreglo[j + 1], arreglo[j]

# Ejemplo de uso:
def main():
    arreglo_numeros = [3, 1, 4, 1, 5, 9, 2, 6, 5]
    print("Arreglo original:", arreglo_numeros)
    ordenar_arreglo(arreglo_numeros)
    print("Arreglo ordenado:", arreglo_numeros)

if __name__ == "__main__":
    main()
