
# El método get busca un elemento a partir de su clave y si no lo encuentra devuelve un valor por defecto
colores = {"amarilo": "yellow", "azul": "blue", "verde": "green"}
print(colores.get('azul', 'No se encuentra'))

# El método keys() genera y retorna una lista de los llaves del diccionario
print(" La lista de keys es :", colores.keys())

# El método value() genera una lista de los valores
print("La lista de valores es :", colores.values())

# El método items() muestra la clave y el valor
print("Mostranto clave y valor con items() :", colores.items())

for clave, valor in colores.items():
    print(clave, valor)

# El método pop() extrae un registro a partir de su key , acepta valor por defecto
print("El valor...usando pop es :", colores.pop("amarillo", "No se encuentra"))

# El método clear() borrar todos los valores
colores.clear()

print("Mostrando diccionario vacío :", colores)
