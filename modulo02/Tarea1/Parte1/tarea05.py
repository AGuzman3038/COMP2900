#Se crea la función
def encontrar_indice(lista, elemento):
    
    try:
        indice = lista.index(elemento)
        return indice
    except ValueError:
        return -1

# Ejemplo de uso:
mi_lista = [10, 20, 30, 40, 50]

#Se le indica que elemento de la lista a buscar e indica en que posición se encuentra
elemento_a_buscar = 30
indice_resultante = encontrar_indice(mi_lista, elemento_a_buscar)

if indice_resultante != -1:
    print(f"El elemento {elemento_a_buscar} se encuentra en el índice {indice_resultante} de la lista.")
else:
    print(f"El elemento {elemento_a_buscar} no se encuentra en la lista.")
