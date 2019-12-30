c1 = {1, 2, 3}
c2 = {3, 4, 5}
c3 = {1, 2, 3, 4, 5}
c4 = {1, 2, 3, 4, 5, 6, 7}


# El método isdisjoint() compreba que un conjunto sea totalmente diferente a otro
print(" Devuelve False cuando porque el valor 3 existe en ambos conjuntos",
      c1.isdisjoint(c2))


print("En este ejemplo devolvería True ya que los conjuntos tiene valores diferentes :", {
      1, 2, 3}.isdisjoint({4, 5, 6}))

# Método issuccest: Comprueba si el conjunto es subconjutno de otro conjunto
print("Devuelve True porque todos los valores del conjunto c3 están el conjunto c4 :", c3.issubset(c4))

# Método issuperset(): Comprueba que el conjunto es contenedor de otro subjunto
print("Devuelve false porque c3 no contiene todos los valores que están el c4",
      c3.issuperset(c4))



