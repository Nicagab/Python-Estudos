N = int(input("Digite um número inteiro: "))
lista = []
i = 0
print(f"Digite {N} números inteiros:")
while i<N:
    e = int(input())
    lista.append(e)
    i += 1
    
print(f"Sua lista: {lista}")

Nr = 0

i = 0

while i<N:
    cont = i+1
    while cont<N:
        if lista[i]==lista[cont]:
            del lista[cont]
            Nr += 1
            N += -1
        cont += 1
    i += 1

print(f"Sua lista possuia {Nr} elementos repetidos.\nLista após a remoção: {lista}")
