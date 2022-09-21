# podemos escribir un archivo con el modo "a"

file = open("file_handling/demo.txt", "a")

file.write("hola inmundo")

file.close()

# Precaucion, el modo "w" borra el contenido anterior
file = open("file_handling/demo.txt", "w")

file.write("hola inmundo")


file.close()
