def ejemplo(* args):
    for dato in args:
        print(dato)


def porNombre(**kwargs):
    print(kwargs)


def porNombrePosicion(*args, **kwargs):
    print(args, kwargs)


ejemplo(2, 4, 5, 6, "Ariel")

porNombre(a="Alex", n=10, b=5)
porNombrePosicion(2, 4, N=5)
