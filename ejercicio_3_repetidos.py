#Entrada.
lista_B = [4, 2, 4, 7, 2, 9]

def eliminar_repetidos(lista):
    lista_sin_repetidos = []
    for elemento in lista:
        if elemento not in lista_sin_repetidos:
            lista_sin_repetidos.append(elemento)
    return lista_sin_repetidos


print(eliminar_repetidos(lista_B))