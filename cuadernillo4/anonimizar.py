# Escribe un función que anonimice el fichero interview.txt. 
# Este fichero contiene una entrevista con Trump, pero su nombre 
# no puede aparecer y hay que cambiarlo a "Mr. X" para anonimizar el fichero. 
# El resultado, será escrito en un fichero anonymous.txt.

f = open("cuadernillo4/interview.txt", mode="r", encoding="utf-8")
f_anonimo = open("cuadernillo4/anonymous.txt", mode="w", encoding="utf-8")

def anonimizar(f, f_anonimo):
    for linea in f:
        f_anonimo.write(linea.replace("Trump", "Mr. X"))

anonimizar(f, f_anonimo)
f.close()
f_anonimo.close()
