
# El método get busca un elemento a partir de su clave y si no lo encuentra devuelve un valor por defecto
colores = {"amarilo": "yellow", "azul": "blue", "verde": "green"}
print(colores.get('azul', 'No se encuentra'))

# El método keys() genera y retorna una lista de los llaves del diccionario
print(" La lista de keys es :", colores.keys())
