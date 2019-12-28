class Pelicula:

    # Contructor de la clase
    def __init__(self, titulo, duracion, lanzamiento):
        self.titulo = titulo
        self.duracion = duracion
        self.lanzamiento = lanzamiento

        print("Se creó la película", self.titulo)

    def __str__(self):
        return "{} lanzando el {} con duración de {} minutos.".format(self.titulo, self.lanzamiento, self.duracion)


class Catalogo:
    peliculas = []

    def __init__(self, peliculas):
        self.peliculas = peliculas

    def mostrar(self):
        for p in self.peliculas:
            print(p)

    def agregarPelicula(self, pelicula):
        self.peliculas.append(pelicula)


peli = Pelicula("El Padrino", 175, 1972)
catalogo = Catalogo([peli])
catalogo = Catalogo(100)
catalogo.mostrar()
catalogo.agregarPelicula(Pelicula("El Padrino : Parte 2", 202, 1975))
