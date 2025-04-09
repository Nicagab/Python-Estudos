from random import randint

N= int(input("Qtde de valores na lista:"))
lista = []
while N!=0:
    e = randint(0,1000)
    lista.append(e)
    N += -1

X = int(input("Digite um número:"))

if X in lista:
    print(f"{X} está presente na lista")
else:
    print(f"{X} não está presente na lista")

print(lista)