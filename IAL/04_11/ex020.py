from random import randint

N = int(input("Digite um número maior que 10: "))

while N<=10:
    N = int(input("Número Inaválido!\nDigite um número maior que 10: "))

lista = []
i = 0

while i<N:
    e = randint(0,100)
    lista.append(e)
    i += 1

print(f"Lista gerada: {lista}")

listaO = []
tamL = 0
i = 0

while i<N:
    cont = 0
    posicao = 0
    while cont<tamL:
        if lista[i]>listaO[cont]:
            posicao += 1
        cont += 1
    listaO.insert(posicao, lista[i])
    i += 1
    tamL += 1

print(f"Lista organizada: {listaO}")
