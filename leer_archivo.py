
#leer el archivo de la noticia.txt

noticia = open("noticia.txt","rt",encoding='utf8')  #rt = readText - lectura

#Cuando abres un archivo en modo "rt", estás indicando que deseas leer datos de texto de ese archivo.
#La letra "r" indica que el archivo se abrirá para lectura, y la "t" indica que el archivo se abrirá en modo de texto.


datos_noticia = noticia.read()
print(datos_noticia)

