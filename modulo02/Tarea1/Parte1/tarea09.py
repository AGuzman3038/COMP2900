import random

def generar_numeros_aleatorios(cantidad, minimo, maximo):

    return [random.randint(minimo, maximo) for _ in range(cantidad)] #se encarga de generar números aleatorios dentro del rango dado

#Se le da valor a las variables, en este caso la cantidad de numeros a dar y dentro de que rango mínimo y máximo debe estar
cantidad_numeros = 5
valor_minimo = 1
valor_maximo = 100

#Se le da valor a una nueva instancia y esta se toma de los valores dados anteriormente
lista_aleatoria = generar_numeros_aleatorios(cantidad_numeros, valor_minimo, valor_maximo)
print(f"La cantidad de números aleatorios será de {cantidad_numeros}, el número menor será de {valor_minimo} y no pasará de {valor_maximo}.")
print(f"Lista de números aleatorios: {lista_aleatoria}")
