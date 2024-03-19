def sumar_elementos_arreglo(arreglo):
    suma_total = 0
    for numero in arreglo:
        suma_total += numero
    return suma_total

# Ejemplo de uso:
def main():
    arreglo_numeros = [1, 2, 3, 4, 5]
    suma_total = sumar_elementos_arreglo(arreglo_numeros)
    print(f"La suma total de los elementos del arreglo es: {suma_total}")

if __name__ == "__main__":
    main()
