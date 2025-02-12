# Escribe una función generadora que devuelva una palabra 
# de un fichero cada vez que es llamada.

f = open("cuadernillo4/palabras.txt", mode="r", encoding="utf-8")

def generar_palabra(f):
    palabras = f.readlines()
    for p in palabras:
        yield p.strip()

gen = generar_palabra(f) 
print(next(gen))