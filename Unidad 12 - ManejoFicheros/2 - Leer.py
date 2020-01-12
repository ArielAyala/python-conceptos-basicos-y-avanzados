from io import open


fichero = open("Unidad 12 - ManejoFicheros/fichero.txt",'r')
texto = fichero.read()

fichero.close()
print(texto)