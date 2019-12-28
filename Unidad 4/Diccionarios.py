datos = {'azul': 'blue', 1: 'uno', 2: 'dos'}
print("Mostrar todo el diccionario :", datos)
print("Mostrar un dato del diccionario por su índice : ", datos[1])

datos['verde'] = 'green'
print("Diccionario actualizado con un valor más :", datos)

del(datos['azul'])
print("El diccionario luego de elimnado un dato por su índice :", datos)

for key, value in datos.items():
    print(key, " -", value)

personajes = []
gandalf = {'Nombre': 'Gandalf', 'Clase': 'Mago', 'Raza': 'Humano'}
legolas = {'Nombre': 'Legolas', 'Clase': 'Arquero', 'Raza': 'Elfo'}
gimli = {'Nombre': 'Gimli', 'Clase': 'Guerero', 'Raza': 'Enano'}

personajes.append(gandalf)
personajes.append(legolas)
personajes.append(gimli)

print("Lista de personajes ", personajes)

