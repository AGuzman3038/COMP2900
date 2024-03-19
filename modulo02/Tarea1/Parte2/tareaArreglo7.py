def calcular_promedio(arreglo):
    if not arreglo:
        return None  # Retorna None si el arreglo está vacío
    
    suma = 0
    cantidad_elementos = 0
    for num in arreglo:
        suma += num
        cantidad_elementos += 1
    
    promedio = suma / cantidad_elementos
    return promedio

# Ejemplo de uso:
def main():
    arreglo_numeros = [1, 2, 3, 4, 5]
    promedio = calcular_promedio(arreglo_numeros)
    if promedio is not None:
        print(f"El promedio de los elementos del arreglo es: {promedio}")
    else:
        print("El arreglo está vacío.")

if __name__ == "__main__":
    main()
