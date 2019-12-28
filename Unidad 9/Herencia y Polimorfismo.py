class Producto:
    def __init__(self, Codigo, Nombre, Precio, Descripcion):
        self.Codigo = Codigo
        self.Nombre = Nombre
        self.Precio = Precio
        self.Descripcion = Descripcion

    def __str__(self):
        return f"Código\t\t{self.Codigo}\n"\
            f"Nombre\t\t{self.Nombre}\n"\
            f"Precio\t\t{self.Precio}\n"\
            f"Descripción\t{self.Descripcion}\n"


class Adorno(Producto):
    pass


class Alimento(Producto):
    Productor = ""
    Distribuidor = ""

    def __str__(self):
        return f"Código\t\t{self.Codigo}\n"\
            f"Nombre\t\t{self.Nombre}\n"\
            f"Precio\t\t{self.Precio}\n"\
            f"Descripción\t{self.Descripcion}\n"\
            f"Productor\t{self.Productor}\n"\
            f"Distribuidor\t{self.Distribuidor}\n"


class Libro(Producto):
    Isbn = ""
    #Autor = ""

    def __str__(self):
        return f"Código\t\t{self.Codigo}\n"\
            f"Nombre\t\t{self.Nombre}\n"\
            f"Precio\t\t{self.Precio}\n"\
            f"Descripción\t{self.Descripcion}\n"\
            f"Isbn\t\t{self.Isbn}\n"\
            f"Autor\t\t{self.Autor}\n"


adorno = Adorno(2034, "Vaso adornado", 15, "Vaso de porcelana")


alimento = Alimento(2034, "Vaso adornado", 15, "Vaso de porcelana")
alimento.Productor = "La Aceitera"
alimento.Distribuidor = "Distribuciones SA"


libro = Libro(2034, "Vaso adornado", 15, "Vaso de porcelana")
libro.Isbn = "Isbn de prueba"
libro.Autor = "Autor de prueba"

productos = [adorno, alimento, libro]


def rebajarProducto(producto, rebaja):
    producto.precio = producto.precio - (producto.precio / 100 * rebaja)


print(alimento, "\n")
rebajarProducto(alimento, 10)
print(alimento)