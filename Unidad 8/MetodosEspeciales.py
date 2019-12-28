class Pelicula:

    # Contructor de la clase
    def __init__(self, titulo, duracion, lanzamiento):
        self.titulo = titulo
        self.duracion = duracion
        self.lanzamiento = lanzamiento

        print("Se creó la película", self.titulo)

    # Destructor de la lcase
    def __del__(self):
        print("Se está borrando la película", self.titulo)

    # Redefiniendo el método string
    def __str__(self):
        return "{} lanzando el {} con duración de {} minutos.".format(self.titulo, self.lanzamiento, self.duracion)

    def __len__(self):
        return self.duracion


pelicula = Pelicula("El Padrino", 175, 1973)

print(str(pelicula))
