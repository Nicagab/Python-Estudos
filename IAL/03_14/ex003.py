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
    soma = soma + nums[i]
    i = i+1

print(f"Total: = {soma}")
