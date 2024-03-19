def combinar_arreglos(arreglo1, arreglo2):
    arreglo_combinado = []
    for elemento in arreglo1:
        arreglo_combinado.append(elemento)
    for elemento in arreglo2:
        arreglo_combinado.append(elemento)
    return arreglo_combinado

# Ejemplo de uso:
def main():
    arreglo1 = [1, 2, 3]
    arreglo2 = [4, 5, 6]
    arreglo_combinado = combinar_arreglos(arreglo1, arreglo2)
    print("Arreglo combinado:", arreglo_combinado)

if __name__ == "__main__":
    main()
