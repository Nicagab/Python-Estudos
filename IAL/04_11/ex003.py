N = int(input("Digite um número entre 0 e 50:"))
A = []

while N<0 or N>50:
    N = int(input("Número Inválido! Digite um número entre 0 e 50:"))

Nc = N

while N!=0:
    e = float(input("Digite um número real:"))
    A.append(e)
    N += -1

i = 0

while Nc!=0:
    print(f"{A[i]}")
    Nc += -1
    i += 1
