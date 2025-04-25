nA = int(input("Tamanho da lista A:"))
nB = int(input("Tamanho da lista B:"))
A = []
B = []

i = 0

while i<nA:
    e = int(input("Digite um número inteiro: (lista A)"))
    A.append(e)
    i += 1

i = 0

while i<nB:
    e = int(input("Digite um número inteiro: (lista B)"))
    B.append(e)
    i += 1

nR = nA+nB
R = A+B

print(f"nR={nR}\nR: {R}")
