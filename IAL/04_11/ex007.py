N = int(input("Quantos valores deseja inserir?"))
if N<=0:
    print("Nenhum valor foi inserido a lista!")
else:
    Lmin = int(input("Digite um valor mínimo:"))
    Lmax = int(input("Digite um valor máximo:"))

    while Lmax<=Lmin:
        print("O valor mínimo deve ser menor que o máximo!")
        Lmin = int(input("Digite um valor mínimo:"))
        Lmax = int(input("Digite um valor máximo:"))

    A = []
    tam = 0

    i = 0

    while i<N:
        e = int(input("Digite um número inteiro:"))
        if e>=Lmin and e<=Lmax:
            A.append(e)
            tam += 1
        i += 1

    if tam==0:
        print("Nenhum valor foi inserido a lista!")
    else:
        print(f"Lista: {A}.\nA lista possui: {tam} itens.")