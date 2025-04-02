num = 1
maior = 0
menor = 0
arquivo = open("ex007.txt", "w")
cont = 0
media = 0

while num>0:
    num = int(input("Digite um número:"))
    if num>0:
        if num>maior or maior==0:
            maior = num
        if num<menor or menor==0:
            menor = num
        media += num
        cont += 1

arquivo.write(f"Maior valor: {maior}\nMenor valor: {menor}\nQtde. de valores apresentados: {cont}\nMédia entre os valores digitados: {media/cont}")
arquivo.close()
print(f"Maior valor: {maior}\nMenor valor: {menor}\nQtde. de valores apresentados: {cont}\nMédia entre os valores digitados: {media/cont}")    
