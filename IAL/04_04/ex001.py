nums = []
num = int(input("Insira um número: "))

while num>0:
    nums.append(num)
    num = int(input("Insira um número: "))

print(f"Números digitados: {nums}")