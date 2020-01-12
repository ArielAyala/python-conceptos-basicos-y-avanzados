from io import open

texto = "Una linea de texto\notra linea con texto"
fichero = open('Unidad 12 - ManejoFicheros/fichero.txt','w')

fichero.write(texto)
fichero.close()
