def cuentaRecresiva(n):
    n -= 1
    if n > 0:
        print(n)
        cuentaRecresiva(n)
    else:
        print("Explotó")

cuentaRecresiva(5)