archivo = "archivo.txt"
f = open(archivo, "w")
f.write("Hola mundo1\n")
f.close()

f2 = open(archivo, "a")
f2.write("Hola mundo2")
f2.close()
