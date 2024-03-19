def contar_apariciones(arreglo, elemento):
    contador = 0
    for num in arreglo:
        if num == elemento:
            contador += 1
    return contador

# Ejemplo de uso:
def main():
    arreglo_numeros = [1, 2, 3, 4, 2, 5, 2]
    elemento_a_contar = 2
    cantidad_apariciones = contar_apariciones(arreglo_numeros, elemento_a_contar)
    print(f"El elemento {elemento_a_contar} aparece {cantidad_apariciones} veces en el arreglo.")

if __name__ == "__main__":
    main()
