""" Problema 2. Frecuencia de palabras en un texto.
Escribe una función que reciba por parámetro una lista de palabras y la ruta a
un fichero de texto y devuelva un diccionario que muestre cuantas veces
aparecen las disƟntas palabras de la lista en el fichero de texto. Haz un pequeño
programa que la ponga a prueba. """


import string

def frecuencia_palabras(lista_palabras, ruta_fichero):
    # Leer el contenido del fichero
    with open(ruta_fichero, 'r', encoding='utf-8') as f:
        texto = f.read()
    
    # Convertir a minúsculas y eliminar puntuación
    texto = texto.lower()
    for signo in string.punctuation:
        texto = texto.replace(signo, "")
    
    palabras_texto = texto.split()
    
    # Crear diccionario de frecuencias
    frecuencias = {}
    for palabra in lista_palabras:
        frecuencias[palabra] = palabras_texto.count(palabra)
    
    # Mostrar ordenado por palabra
    for palabra in sorted(frecuencias):
        print(f"{palabra}: {frecuencias[palabra]}")
    
    return frecuencias

# Ejemplo
frecuencia_palabras(["python", "datos", "inteligencia", "programación"], "texto_prueba_problema2.txt")
