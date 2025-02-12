# Escribe una función que recibe el nombre de un fichero 
# (cada línea puede tener varias palabras) y una letra, 
# y que muestre por pantalla las palabras del fichero que 
# contienen la letra.

f = open("cuadernillo4/palabras.txt", mode="r", encoding="utf-8")

def contiene_letra(f):
    letra = input("Introduce una letra: ")
    palabras = f.readlines()
    for p in palabras:
        p = p.strip()
        if letra in p:
            print(p)
contiene_letra(f)
f.close()
