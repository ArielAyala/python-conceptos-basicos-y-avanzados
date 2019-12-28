# Definir un conjunto vacio
conjunto = set()
print("Conjunto vacio :", conjunto)

# Conjunto con datos
conjuntoDatos = {1, 2, 3}
print("Conjunto con datos :", conjuntoDatos)

# Agregar un dato con add
conjuntoDatos.add(4)
conjuntoDatos.add(0)
conjuntoDatos.add("B")
conjuntoDatos.add("C")
conjuntoDatos.add("A")
conjuntoDatos.add("Texto")
print("Conjunto de datos luego de agregar dos valores :", conjuntoDatos)

# Dato importante, en un conjunto no se puede repetir datos, si tiene datos repetidos los elimina

nombres = {"Ariel", "Ariel", "ariel"}
print("Verificando si Alex está en el conjunto nombres :", "Alex" in nombres)
print("Datos del conjunto nombres :", nombres)

# Conversiones con listas
lista = [1, 2, 3, 3, 4, 2, 5]
print(lista)

# Agregar un conjunto una lista
conjuntoNum = set(lista)
print("El conjunto de números de la lista es :", conjuntoNum)

# Agregar una lista un conjunto
listaDelConjunto = list(conjuntoNum)
print("Lista a partir del conjunto :", listaDelConjunto)
