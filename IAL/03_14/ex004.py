nums = []

num = int(input("Digite quantos números quer somar:"))
cont = 0

while cont<num:
    n = float(input("Digite um número:"))
    nums.append(n)
    cont = cont+1
    

i = 0
soma = 0

while i<len(nums):
    if nums[i]>0:
        soma = soma + nums[i]
        i = i+1
    else:
        i = i+1

print(f"Total dos números positivos: = {soma}")
