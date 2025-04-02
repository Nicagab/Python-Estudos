lista = input("Digite 10 elementos: ").split()
while len(lista)!=10:
    lista = input("Lista inválida, Digite 10 elementos: ").split()
listaI = []
i = len(lista)-1

while i>=0:
    listaI += lista[i]
    i += -1
    
print(listaI)