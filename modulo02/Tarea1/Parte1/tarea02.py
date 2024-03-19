#Se define la función
def area_triangulo(base, altura):
    #El 0.5 es equivalente multiplicar la base por la altura y dividirlo entre 2
    return 0.5 * base * altura

#Se le pide al usuario que ingrese los valores.
base_triangulo = float(input("Ingrese la base del triangulo: "))
altura_triangulo = float(input("Ingrese la altura del triangulo: "))

#Se le da valor a la variable con el resultado de la función.
area_resultante = area_triangulo(base_triangulo, altura_triangulo)
print(f"El área del triángulo con base {base_triangulo} y altura {altura_triangulo} es: {area_resultante}")

