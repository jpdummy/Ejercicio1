""" Problema 3. Trabajo con conjuntos
Escribe una función que reciba dos listas de enteros y devuelva un diccionario
con la siguiente información (ES OBLIGATORIO USAR CONJUNTOS PARA
CALCULARLOS)
1. La intersección de ambos conjuntos (elementos comunes).
2. La unión de ambos conjuntos (todos los elementos sin duplicados).
3. La diferencia simétrica (elementos que están en uno u otro conjunto,
pero no en ambos) """


def operar_conjuntos(lista1, lista2):
    conjunto1 = set(lista1)
    conjunto2 = set(lista2)
    
    resultado = {
        "interseccion": conjunto1 & conjunto2,
        "union": conjunto1 | conjunto2,
        "diferencia_simetrica": conjunto1 ^ conjunto2
    }
    
    return resultado

# Ejemplo
print(operar_conjuntos([1, 2, 3], [3, 4, 5]))
