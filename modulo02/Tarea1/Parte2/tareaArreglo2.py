def encontrar_maximo_arreglo(arreglo):
    if not arreglo:
        return None  # Retorna None si el arreglo está vacío
    
    maximo = arreglo[0]  # Inicializa el máximo con el primer elemento del arreglo
    for elemento in arreglo:
        if elemento > maximo:
            maximo = elemento  # Actualiza el máximo si el elemento actual es mayor
    return maximo

# Ejemplo de uso:
def main():
    arreglo_numeros = [1, 6, 3, 8, 2, 10]
    maximo = encontrar_maximo_arreglo(arreglo_numeros)
    if maximo is not None:
        print(f"El máximo elemento del arreglo es: {maximo}")
    else:
        print("El arreglo está vacío.")

if __name__ == "__main__":
    main()
