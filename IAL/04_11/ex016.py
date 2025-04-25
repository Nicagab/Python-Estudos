N = int(input("Digite um número inteiro: "))
lista = []
i = 0

while i<N:
    e = int(input("Digite um número inteiro:"))
    cont = 0
    nR = False
    while cont!=i and not nR:
        if e==lista[cont]:
            print("Este número já foi digitado!")
            nR = True
        cont += 1
    if not nR:
        lista.append(e)
        i += 1

print(lista)
        
