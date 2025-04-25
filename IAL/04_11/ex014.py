i = 0
A = []
B = []
C = []

while i<10:
    e = int(input("Digite um elemento para a lista A: "))
    e2 = int(input("Digite um elemento para a lista B: "))

    A.append(e)
    B.append(e2)

    i += 1

C = A+B

print(f"Lista A: {A}\nLista B: {B}\nLista unificada: {C}")
