n = int(input("Digite um número: "))
maior = 0
menor = 0

i = 0
num = 0

while i<n:
    num = float(input("Digite um número: "))
    if num<=0:
        print("Número inválido") 
    if num>maior or maior==0:
        maior = num
    if num<menor or menor==0:
        menor = num
    i += 1

arquivo = open("ex004.txt", "w")
arquivo.write(f"Maior número digitado: {maior}\nMenor número digitado: {menor}")
arquivo.close()
print(f"Maior número digitado: {maior}\nMenor número digitado: {menor}")
