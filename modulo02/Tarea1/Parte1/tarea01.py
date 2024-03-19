#Se define la función
def mayor(a, b):
    #Se abre una condición
    if a > b:
        return a
    else:
        return b

#Se le pide al usuario que ingrese los valores
numero1 = int(input("Ingrese el primer valor entero: "))
numero2 = int(input("Ingrese el segundo valor entero: "))

resultado = mayor(numero1, numero2)
#Se da los valores ingresados y el resultado de cual es mayor.
print(f"El mayor entre {numero1} y {numero2} es: {resultado}")

