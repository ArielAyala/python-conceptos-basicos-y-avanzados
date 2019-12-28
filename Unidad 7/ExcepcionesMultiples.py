while True:
    try:
        n = float(input("Intruduce un número :"))
        print(5/n)
    except TypeError:
        print("No se puede dividir el número entre una cadena")
    except ValueError:
        print("Deve introducir un número")
    except ZeroDivisionError:
        print("No se puede dividir por cero")
    except Exception as e:  # guardamos la excepción en una variable e
        print("Ocurrió un error => ", type(e).__name__)
    else:
        print("Proceso exitoso")
        break