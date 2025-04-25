N = int(input("Digite um número: "))
lista = []
i = 0
P = 2
while i<N:
    cont = 2
    while cont<=P:
        print(cont)
        if P==2:
                lista.append(P)
                P += 1
                i += 1
                cont += 1
        if cont==2:
            cont+=1
        if P%cont==0 and cont!=P:
                P += 2
        cont += 2
    lista.append(P)
    i+=1
    P+=2

print(lista)
    
