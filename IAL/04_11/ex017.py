nA = int(input("Tamanho da lista A:"))
nB = int(input("Tamanho da lista B:"))
A = []
B = []

i = 0

while i<nA:
    e = int(input("Digite um número inteiro: (lista A)"))
    cont = 0
    nR = False
    while cont!=i and not nR:
        if e==A[cont]:
            print("Este número já foi digitado!")
            nR = True
        cont += 1
    if not nR:
        A.append(e)
        i += 1

i = 0

while i<nB:
    e = int(input("Digite um número inteiro: (lista B)"))
    cont = 0
    nR = False
    while cont!=i and not nR:
        if e==B[cont]:
            print("Este número já foi digitado!")
            nR = True
        cont += 1
    if not nR:
        B.append(e)
        i += 1

nR = nA
R = A

i= 0

while i<nB:
    e = B[i]
    cont = 0
    repetido = False
    while cont!=nR and not repetido:
        if e==R[cont]:
            repetido = True
        cont += 1
    if not repetido:
        R.append(e)
        nR += 1
    i += 1

print(f"nR={nR}\nR: {R}")
