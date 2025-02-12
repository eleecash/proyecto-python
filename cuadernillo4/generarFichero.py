# Escribe un programa que genere un fichero de texto con los 
# números del 1 al 5000 y sus cuadrados.

f = open("numeros.txt", mode="wt", encoding="utf-8")

for i in range(1, 5001):
    f.write(f"{i} {i**2}\n")