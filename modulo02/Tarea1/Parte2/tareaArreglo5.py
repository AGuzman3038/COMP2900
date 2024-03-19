def eliminar_elemento(arreglo, elemento):
    nuevo_arreglo = []
    for num in arreglo:
        if num != elemento:
            nuevo_arreglo.append(num)
    return nuevo_arreglo

# Ejemplo de uso:
def main():
    arreglo_numeros = [1, 2, 3, 4, 5]
    elemento_a_eliminar = 3
    nuevo_arreglo = eliminar_elemento(arreglo_numeros, elemento_a_eliminar)
    print("Arreglo original:", arreglo_numeros)
    print("Arreglo con el elemento eliminado:", nuevo_arreglo)

if __name__ == "__main__":
    main()
