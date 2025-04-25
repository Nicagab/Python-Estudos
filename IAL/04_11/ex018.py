min = int(input("Insira um valor mínimo:"))
max = int(input("Insira um valor máximo:"))

while max<=min:
    max = int(input("Valor máximo deve ser maior que o mínimo!Insira um valor máximo:"))

if min%7!=0:
    num = min+(7-min%7)
else:
    num = min

lista = []
while num<=max:
    lista.append(num)
    num += 7

print(lista)