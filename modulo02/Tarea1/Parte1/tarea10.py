def contar_apariciones_letra(cadena, letra):
    cadena = cadena.lower()
    letra = letra.lower()
    contador = 0
    for caracter in cadena:
        if caracter == letra:
            contador += 1
    return contador

# Se da valor a la variable texto y se le indica qué letra buscar
texto = "Hola, ¿cómo estás?"
letra_buscada = "o"

# Se llama a la función 
apariciones = contar_apariciones_letra(texto, letra_buscada)
print(f"La letra '{letra_buscada}' aparece {apariciones} veces en el texto.")

