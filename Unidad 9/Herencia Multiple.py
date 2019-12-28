class A:
    def __init__(self):
        print("Clase A")

    def a(self):
        print("Método Clase A")


class B:
    def __init__(self):
        print("Clase B")

    def b(self):
        print("Método Clase B")


class C(A, B):
    def c(self):
        print("Soy clase c")


c = C()
c.a()
c.b()
c.c()