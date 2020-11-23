from io import open


# forma de leer un archivo de texto
archivo_texto = open("archivo.txt", "r")

texto = archivo_texto.read()

archivo_texto.close()

print(texto)

# como sobre escribir un archivo de texto en python

archivito = open("archivo.txt", "w")

frase = "nuevo texto"

archivito.write(frase)


archivito.close()

# como agregar texto a un archivo de texto en python
otroArchivo = open("archivo.txt", "a")
otroArchivo.write("no se como haser un salto de linea porque no puedo sacar la puta barra invertida")
otroArchivo.close()

# leer el archivo de texto modificado

nuevamente = open("archivo.txt", "r")

varia = nuevamente.read()

nuevamente.close()

print(varia)


