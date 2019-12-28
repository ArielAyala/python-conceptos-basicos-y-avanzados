class Ejemplo:
    __atributo_privato = "Atributo privado"

    def __metodo_privado(self):
        print("Ejecutando el método privado")

    def metodo_publico(self):
        print("Ejecutando el método publico")

e = Ejemplo()
e.metodo_publico()
