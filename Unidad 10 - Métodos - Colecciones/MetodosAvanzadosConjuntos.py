
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
