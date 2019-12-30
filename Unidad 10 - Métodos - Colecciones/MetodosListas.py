# Añade un item al final de la lista
lista = [1, 2, 3, 4, 5]
lista.append(6)
print(lista)

# Vacia los items de una lista con clear
lista.clear()
print(lista)

# Une una lista a otra con extend
l1 = [1, 2, 3]
l2 = [4, 5, 6]
l1.extend(l2)
print("Al extender la lista2 a la lista 1 el resultado es :", l1)

# Cuenta con count el número de veces que aparece un ítem
nombre = ["hola", "mundo", "mundo"]
print("El número de veces que aparece el texto es :", nombre.count("hola"))

# El método index devuelve el índice en el que aparece un texto(error si no aparece)
print("La posición en la que aparece es el texto es:", nombre.index("mundo"))

# El método insert() Agrega un valor a la lista en un índice específico
l = [1, 2, 2, 2, 3]
l.insert(0, 10)
print(l)

# El método pop extrae un ítem de la lista y lo borra
l.pop()
print(l)

# El método remover() elimina el primer dato cuyo valor coincida con el texto ingresado
l.remove(1)
print("Removiendo el valor 1 de la lista l:", l)

# El método reverse() invierte el orden a la lista
print("La lista la con las posiciones invertidas es:", l)

# El método sort() ordena los valores de la lista de forma ascendente
n = [30, 40, 20, 10, 100]
n.sort()
print("Lista n con valores ordenados", n)

# Mayor a menor
n.sort(reverse=True)
print("Ordenada de mayor a menor", n)
