class Galletas:
    chocolate = False
    sabor = None
    color = None
    forma = "Cuadrado"

    def __init__(self, sabor=None, color=None):
        self.sabor = sabor
        self.color = color
        if sabor is not None and color is not None:
            print("Se creo una Galleta {} de sabor {}". format(sabor, color))

    def chocolatear(self):
        self.chocolate = True

    def tieneChocolate(self):
        if (self.chocolate):
            print("Soy galleta con chocolate")
        else:
            print("Son galleta sin chocolate")


galleta = Galletas("Salada", "Naranja")
galleta.chocolatear()

print(galleta.chocolate)
