
archivo = open ("archivo_de_prueba.txt","wt")  # wt = WriteText - Escribir texto

#Cuando abres un archivo en modo "wt", estás indicando que deseas escribir datos de 
#texto en ese archivo. Si el archivo no existe, se creará; si ya existe, su contenido 
#se truncará (es decir, se eliminará todo su contenido anterior) y se escribirán los 
#nuevos datos desde el principio.



contenido = "Línea1 hola amigos como están?\nLínea2 Bienvenido a la UNTELS."

archivo.write(contenido)

archivo.close()
