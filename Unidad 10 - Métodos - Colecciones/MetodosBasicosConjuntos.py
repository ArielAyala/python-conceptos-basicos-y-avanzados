# Añade un ítem a un conjunto, si ya existe no lo añade

c = set()

c.add(1)
c.add(2)
c.add(3)
c.add(4)

print("El conjunto c :", c)

# El método discard borra el ítem de un conjunto
c.discard(1)

print("El conjunto c, borrado el valor 1 :", c)

# El método copy() devuelva una copia del conjunto
c1 = {1, 2, 3, 4}
c2 = c1.copy()

print("Los conjuntos c1 y c2 :", c1, c2)

# El método crear() borra los ítems de un conjunto
c2.clear()
print("Items de conjunto c2 borrados :", c2)
