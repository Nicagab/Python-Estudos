#Salarios - Entrega N2.A

arquivo = open('CALCULO.txt', 'w')
SalBruto = float(input())
salarios = []

while SalBruto != 0.00:
    salarios.append(SalBruto)
    SalBruto = float(input())

def CalcularAliqInss(e):
    if e>=8157.42:
        return 'Teto'
    elif e<=1518:
        return 7.5/100
    elif e <=2793.88:
        return 9/100
    elif e <=4190.84:
        return 12/100
    elif e <= 8157.41:
        return 14/100

def CalcularValInss(e):
    if e>=8157.42:
        return 951.62
    elif e<=1518:
        AliqINSS = 7.5/100
        DeduçãoINSS = 0
    elif e <=2793.88:
        AliqINSS = 9/100
        DeduçãoINSS = 22.77
    elif e <=4190.84:
        AliqINSS = 12/100
        DeduçãoINSS = 106.59
    elif e <= 8157.41:
        AliqINSS = 14/100
        DeduçãoINSS = 190.40

    return (e * AliqINSS - DeduçãoINSS)

def CalcularAliqIR(e):
    if e - CalcularValInss(e) > 4664.68:
        return 27.5/100
    elif e - CalcularValInss(e) <= 2259.20:
        return 0
    elif e - CalcularValInss(e) <= 2826.65:
        return 7.5/100
    elif e - CalcularValInss(e) <= 3751.05:
        return 15/100
    elif e - CalcularValInss(e) <= 4664.68:
        return 22.5/100

def CalcularValIR(e):
    if e - CalcularValInss(e) > 4664.68:
        DeduçãoIR = 896
    elif e - CalcularValInss(e) <= 2259.20:
        DeduçãoIR = 0
    elif e - CalcularValInss(e) <= 2826.65:
        DeduçãoIR = 169.44
    elif e - CalcularValInss(e) <= 3751.05:
        DeduçãoIR = 381.44
    elif e - CalcularValInss(e) <= 4664.68:
        DeduçãoIR = 662.77
    
    return ((e - CalcularValInss(e))*CalcularAliqIR(e) - DeduçãoIR)

def CalcularLiquido(e):
    return e - CalcularValInss(e) - CalcularValIR(e)

salarios.sort()

print('{:>14}{:>14}{:>14}{:>14}{:>14}{:>14}{:>14}'.format("Bruto","AliqINSS","ValINSS","Base IR","Aliq IR","Val IR","Líquido"))
arquivo.write('{:>14}{:>14}{:>14}{:>14}{:>14}{:>14}{:>14}\n'.format("Bruto","AliqINSS","ValINSS","Base IR","Aliq IR","Val IR","Líquido"))
for salario in salarios:
    if type(CalcularAliqInss(salario))==str:
        print(f'{salario:>14.2f}{CalcularAliqInss(salario):>14}{CalcularValInss(salario):>14.2f}{salario - CalcularValInss(salario):>14.2f}{CalcularAliqIR(salario):>14.2f}{CalcularValIR(salario):>14.2f}{CalcularLiquido(salario):>14.2f}')
        arquivo.write(f'{salario:>14.2f}{CalcularAliqInss(salario):>14}{CalcularValInss(salario):>14.2f}{salario - CalcularValInss(salario):>14.2f}{CalcularAliqIR(salario):>14.2f}{CalcularValIR(salario):>14.2f}{CalcularLiquido(salario):>14.2f}\n')
    else:
        print(f'{salario:>14.2f}{CalcularAliqInss(salario):>14.2f}{CalcularValInss(salario):>14.2f}{salario - CalcularValInss(salario):>14.2f}{CalcularAliqIR(salario):>14.2f}{CalcularValIR(salario):>14.2f}{CalcularLiquido(salario):>14.2f}')
        arquivo.write(f'{salario:>14.2f}{CalcularAliqInss(salario):>14.2f}{CalcularValInss(salario):>14.2f}{salario - CalcularValInss(salario):>14.2f}{CalcularAliqIR(salario):>14.2f}{CalcularValIR(salario):>14.2f}{CalcularLiquido(salario):>14.2f}\n')

print('\nFim dos Dados')
arquivo.write('\n\nFim dos Dados')
arquivo.close()