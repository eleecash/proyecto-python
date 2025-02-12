# Escribe un programa que lee el nombre del fichero de texto
# del teclado y muestra por pantalla el texto codificado de 
# forma que sólo las letras minúsculas se sustituyen por las 
# siguientes según el abecedario (una a por una b, una b por 
# una c, etc.).

f = open(input("Introduce el nombre del fichero: "), mode="r", encoding="utf-8")

def codificado(f):
    texto = f.read()
    texto_codificado = ""
    for letra in texto:
        if letra.islower():
            letra = chr(ord(letra) + 1)
        texto_codificado += letra
    return texto_codificado

print(codificado(f))