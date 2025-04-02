lista1 = input("Digite 10 números: ").split()
while len(lista1)!=10:
    lista1 = input("Lista inválida, Digite 10 números: ").split()
lista2 = input("Digite mais 10 números: ").split()
while len(lista2)!=10:
    lista2 = input("Lista inválida, Digite 10 números: ").split()

lista3 = []
i = 0
while i<len(lista1):
    lista3.append(int(lista1[i]))
    i += 1
i = 0
while i<len(lista2):
    lista3.append(int(lista2[i]))
    i += 1

print(lista3)