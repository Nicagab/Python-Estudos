Lmin = int(input("Digite um valor mínimo:"))
Lmax = int(input("Digite um valor máximo:"))

while Lmax<=Lmin:
    print("O valor mínimo deve ser menor que o máximo!")
    Lmin = int(input("Digite um valor mínimo:"))
    Lmax = int(input("Digite um valor máximo:"))

A = []
tam = 0

i = 0

while i<10:
    e = int(input("Digite um número inteiro:"))
    if e>=Lmin and e<=Lmax:
        A.append(e)
        tam += 1
    i += 1

print(f"Lista: {A}.\nA lista possui: {tam} itens.")