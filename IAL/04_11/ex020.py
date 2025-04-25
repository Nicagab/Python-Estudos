from random import randint

N = int(input("Digite um número maior que 10: "))

while N<=10:
    N = int(input("Número Inaválido!\nDigite um número maior que 10: "))

lista = []
i = 0

while i<N:
    e = randint()
    lista.append(e)
    i += 1

print("Lista gerada: {lista }")