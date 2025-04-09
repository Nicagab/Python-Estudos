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
    tamA = 0
    R = []
    tamR = 0
    i = 0

    while i<N:
        e = int(input("Digite um número inteiro:"))
        if e>=Lmin and e<=Lmax:
            A.append(e)
            tamA += 1
        else: 
            R.append(e)
            tamR += 1
        i += 1

    if tamA==0:
        print("Todos os valores inseridos foram rejeitados!")
    else:
        print(f"Lista Aceitos: {A}.\nA lista possui: {tamA} itens.")
    if tamR==0:
        print("Todos os valores inseridos foram aceitos!")
    else:
        print(f"Lista Rejeitados: {R}.\nA lista possui: {tamR} itens.")