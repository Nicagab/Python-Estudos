arquivo = open('vendas.txt', "r")
codigos = []  
totais = []
vendas = arquivo.read().split('\n')
i=0
while i<len(vendas):
    partes = vendas[i].split(';')
    cod = int(partes[0])
    qtde = int(partes[1])
    preco = float(partes[2])
    
    if codigos.count(cod)<=0:
        codigos.append(cod)
        totais.append(qtde*preco)
    else:
        cont = codigos.index(cod)
        totais[cont] += qtde*preco

    i += 1

cod = int(input("Digite o código: "))

while cod>0:
    if codigos.count(cod)>0:
        print(f"Total vendo do produto {cod} = R$ {totais[codigos.index(cod)]:.2f}")
    elif cod<10000 or cod>21000:
        print(f"{cod} Código inválido (deve ser entre 10000 e 21000)")
    else:
        print(f"Total vendo do produto {cod} = R$ 0.00")
    cod = int(input("Digite o código: "))

print("Fim do programa")
arquivo.close()  