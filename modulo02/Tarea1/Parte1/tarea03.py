#Se define la funcion 
def fahrenheit_a_celsius(fahrenheit):

    celsius = (fahrenheit - 32) * 5/9
    return celsius

#Se le pide al usuario que ingrese la temperatura
temperatura_fahrenheit = float(input("Ingrese la temperatura en Fahrenheit: "))

#Se llama a la función 
temperatura_celsius = fahrenheit_a_celsius(temperatura_fahrenheit)
#Se da la temperatura ingresada y convertida a celsius
print(f"{temperatura_fahrenheit} grados Fahrenheit son equivalentes a {temperatura_celsius:.2f} grados Celsius")
