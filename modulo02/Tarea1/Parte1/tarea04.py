def promedio(lista_numeros):

    if not lista_numeros:
        return None  # Retorna None si la lista está vacía para evitar divisiones por cero

    suma = 0
    cantidad_elementos = len(lista_numeros)
    
    for numero in lista_numeros:
        suma += numero

    promedio_resultante = suma / cantidad_elementos

    return promedio_resultante

# Lista de números
numeros = [5, 10, 15, 20, 25]

# Calcular el promedio y mostrar el resultado
resultado_promedio = promedio(numeros)

if resultado_promedio is not None:
    print(f"El promedio de la lista {numeros} es: {resultado_promedio}")
else:
    print("La lista está vacía. No se puede calcular el promedio.")