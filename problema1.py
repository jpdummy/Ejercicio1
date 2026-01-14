""" Problema 1. Procesamiento de una lista de enteros.
Crea una función que reciba una lista de enteros por parámetro y devuelva otra
lista, de acuerdo a las siguientes acciones:
1. Eliminar los números negaƟvos de la lista.
2. Eliminar los valores que están repeƟdos, quedándonos con uno de ellos.
3. Ordenar los números resultantes de menor a mayor. """

def procesar_lista(lista):
    # 1. Eliminar negativos
    lista = [num for num in lista if num >= 0]
    # 2. Eliminar repetidos
    lista = list(set(lista))
    # 3. Ordenar
    lista.sort()
    return lista

# Ejemplo
print(procesar_lista([4, -1, 2, 4, 3, -5, 2]))  # Resultado: [2, 3, 4]
