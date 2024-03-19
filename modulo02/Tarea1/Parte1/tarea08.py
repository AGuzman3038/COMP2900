def contar_vocales(cadena):
    vocales = "aeiouAEIOUáéíóú"
    cantidad_vocales = 0
    for letra in cadena:
        if letra in vocales:
            cantidad_vocales += 1
    return cantidad_vocales

texto = "Hola, ¿cómo estás?"

cantidad_vocales = contar_vocales(texto)
print(f"La cantidad de vocales en el texto, {texto}, es de: {cantidad_vocales}")
