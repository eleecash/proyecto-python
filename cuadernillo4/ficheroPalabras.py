# Escribe una función que reciba el nombre de un fichero que 
# contiene palabras (cada línea tiene una palabra) y que devuelva la 
# palabra que tiene una longitud máxima y su longitud.

f = open("cuadernillo4/palabras.txt", mode="r", encoding="utf-8")

def palabra_mas_larga(f):
    palabras = f.readlines()
    longitud = 0
    palabra = ""
    for p in palabras:
        p = p.strip()
        if len(p) > longitud:
            longitud = len(p)
            palabra = p
    return palabra, longitud

print(palabra_mas_larga(f))