def verificarLinha(codigo):
    if len(codigo)!=7:
        return "invalida"
    linha = int(codigo[:3])
    if linha>99 and linha<400:
        return "infantil"
    elif linha<800:
        return "feminina"
    elif linha<1000:
        return "masculina"
    else:
        return "invalida"

print("Código   Qtde    Preço Unit.")

produto = input()
infantil = 0
feminina = 0
masculina = 0
invalidos = []

while produto!="0":
    partes = produto.split()
    cod = partes[0]
    qtde = int(partes[1])
    precoU = float(partes[2].replace(",", "."))
    if verificarLinha(cod)=="infantil":
        infantil += precoU*qtde
    elif verificarLinha(cod)=="feminina":
        feminina += precoU*qtde
    elif verificarLinha(cod)=="masculina":
        masculina += precoU*qtde
    else:
        invalidos.append(cod)
    produto = input()

total = f"{(infantil+feminina+masculina):.2f}"
infantil = f"{infantil:.2f}"
feminina = f"{feminina:.2f}"
masculina = f"{masculina:.2f}"

print(f"\nSubTotais")
print(f"    Linha infantil = {infantil.replace(".",",")}")
print(f"    Linha feminina = {feminina.replace(".",",")}")
print(f"    Linha masculina = {masculina.replace(".",",")}\n")
print(f"Total Geral = {total.replace(".",",")}\n")
print("Inconsistencias")
if len(invalidos)>0:
    for invalido in invalidos:
        print(f"    codigo invalido: {invalido}")
else:
    print(f"    nao ha inconsistencias")