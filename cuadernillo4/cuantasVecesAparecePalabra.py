# Escribe una función que reciba el nombre de 
# un fichero y que muestre por pantalla cuántas 
# veces aparece cada palabra.

f = open("cuadernillo4/palabras.txt", mode="r", encoding="utf-8")

def cuantas_veces_aparece_palabra(f):
    palabras = f.readlines()
    diccionario = {}
    for p in palabras:
        p = p.strip()
        if p in diccionario:
            diccionario[p] += 1
        else:
            diccionario[p] = 1
    return diccionario
print(cuantas_veces_aparece_palabra(f))