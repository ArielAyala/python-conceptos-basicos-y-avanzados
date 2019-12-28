try:
    n = None

    if n is None:
        # print("Erro!!. No se permite valor nulo")
        raise ValueError("Erro!!. No se permite valor nulo")
except ValueError:
    print("No se permite valor nulo")
