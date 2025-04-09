from random import randint
N = int(input("Digite um número entre 0 e 50:"))
A = []
POS = []
NEG = []

while N<0 or N>50:
    N = int(input("Número Inválido! Digite um número entre 0 e 50:"))

Nc = N

while N!=0:
    e = float(input("Digite um número:"))
    A.append(e)
    N += -1

contN = 0
contP = 0
i = 0

while Nc!=0:
    if A[i]>=0:
        POS.append(A[i])
        contP += 1
    else:
        NEG.append(A[i])
        contN += 1
    Nc += -1
    i += 1

i = 0
print("Números negativos:")
while contN!=0:
    print(NEG[i])
    i += 1
    contN += -1

i = 0
print("Números positivos e zeros:")
while contP!=0:
    print(POS[i])
    i += 1
    contP += -1

