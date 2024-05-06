
archivo = open("noticia.txt","at")

#En Python, "at" es un modo de apertura de archivo que se utiliza para abrir un archivo
# en modo de añadir texto al final. La letra "a" indica que el archivo se abrirá en modo
# de añadir (append), y la "t" indica que el archivo se abrirá en modo de texto.

#\n es para agregar el contenido en una linea al final

contenido = "\nFuente : RPP"

archivo.write(contenido)

archivo.close()

