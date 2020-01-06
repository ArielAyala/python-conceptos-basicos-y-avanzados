
# El método union() uno un conjunto con otro conjunto y devuelve el resultado en un nuevo conjunto
c1 = {1, 2, 3}
c2 = {3, 4, 5}

c3 = c1.union(c2)
print(c3)

# El método update() uno un conjunto a otro
c1.update(c2)
print(c1)

# encuentra los elementos no comunes entre dos conjuntos
c1 = {1, 2, 3}
c2 = {3, 4, 5}

print(c1.difference(c2))

# El método difference_update() Guarda en el conjunto los elementos no comunes entre dos conjuntos
print(c1.difference_update(c2))

# El método intersection() guarda un conjunto con los elemenos comunes de dos conjuntos
c1 = {1, 2, 3}
c2 = {3, 4, 5}

print("Los elementos comunes son :", c1.intersection(c2))

# El método intersection_update() guarda en el conjunto los valores comunes de dos conjuntos
c1.intersection_update(c2)
print(c1)

# El método symmetric_difference() devuelve los elementos simétricamente diferentes entre dos conjuntos
c1 = {1, 2, 3}
c2 = {3, 4, 5}
print("Los valores diferentes entre los conjuntos son :",
      c1.symmetric_difference(c2))



