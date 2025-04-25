num = int(input("Digite um número:"))
lista = []
tamL = 0

while num!=0:
    i = 0
    posicao = tamL
    while i<tamL and posicao==tamL:
        if lista[i]>num:
            posicao = i
        i += 1
    lista.insert(posicao,num)
    tamL += 1
    num = int(input("Digite um número:"))

if tamL == 0:
    print("Nenhum número maior que 0 foi digitado!")
else:
    print(f"Números digitados em ordem crescente: {lista}")
