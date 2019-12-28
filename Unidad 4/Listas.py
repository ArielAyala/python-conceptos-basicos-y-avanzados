numeros = [1, 2, 3, 4, 5]
datos = [5, "cadena", 5.5, "texto"]

print("Numeros", numeros)
print("Datos", datos)

# Mostramos datos de la lista por índice
print("Mostramos datos de la lista por índice :", datos[-1])

# Mostramos datos por Slicing
print("Mostramos datos por Slicing :", datos[0:2])

# Suma de Listas
listas = numeros + datos
print("La suma de las listas es :", listas)

# Mutabilidad
pares = [0, 2, 4, 5, 8, 10]
pares[3] = 6

print("Lista de pares, mutando un valor :", pares)

# Funciones o métodos de Listas
c = len(pares)
print("La función 'len' cuenta cuandos datos tiene la lista, ejemplo la lista pares :", c)

pares.append(12)
print("La función 'append' agregar un dato al final de la lista, ejemplo :", pares)
