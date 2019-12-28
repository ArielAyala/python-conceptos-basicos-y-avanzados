n = int("10")
print(n)

f = float("10.5")
print(f)

c = "Un texto y dos números " + str(10) 

print(bin(10))

ariel = 3
ana = 2
sumaTexto = "ariel + ana + 10"

print(type(sumaTexto))
print(eval(sumaTexto))

def metodo(*args):
    for valor in args:
        print("El valor es :",valor)

metodo(2,3,"Ana",[1,2,3])
