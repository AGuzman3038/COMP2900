def buscar_elemento(arreglo, elemento):
    for i in range(len(arreglo)):
        if arreglo[i] == elemento:
            return i  # Retorna la posición del elemento si se encuentra
    return -1  # Retorna -1 si el elemento no se encuentra

# Ejemplo de uso:
def main():
    arreglo_numeros = [1, 2, 3, 4, 5]
    elemento_buscado = 3
    indice = buscar_elemento(arreglo_numeros, elemento_buscado)
    if indice != -1:
        print(f"El elemento {elemento_buscado} se encuentra en la posición {indice}.")
    else:
        print(f"El elemento {elemento_buscado} no se encuentra en el arreglo.")

if __name__ == "__main__":
    main()
