def invertir_cadena(cadena):
    cadena_invertida = ""
    for caracter in cadena:
        cadena_invertida = caracter + cadena_invertida
    return cadena_invertida

# Ejemplo de uso:
texto_original = "Hola, mundo!"

texto_invertido = invertir_cadena(texto_original)
print(f"Texto original: {texto_original}")
print(f"Texto invertido: {texto_invertido}")
