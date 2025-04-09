from random import randint

N= int(input("Qtde de valores na lista:"))
Nc = N
lista = []
while N!=0:
    e = randint(0,1000)
    lista.append(e)
    N += -1

print(f"Lista gerada: {lista}")

X = int(input("Digite um número:"))
pos = []
qtde = 0
i = 0

while i<Nc:
    if X == lista[i]:
        pos.append(i)
        qtde += 1
    i += 1

if qtde>0:
    print(f"{X} está na lista gerada, nas posições: {pos}")
else:
    print(f"{X} não está na lista gerada!")
