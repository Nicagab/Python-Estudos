nums = []

num = int(input("Digite um número: (Digite 0 para terminar)"))

while num!=0:
    nums.append(num)
    num = int(input("Digite um número: (Digite 0 para terminar)"))

i = 0
somaP = 0
somaN = 0
while i<len(nums):
    if nums[i]>0:
        somaP = somaP + nums[i]
        i = i+1
    else:
        somaN = somaN + nums[i]
        i = i+1

print(f"Total dos positivos = {somaP}")
print(f"Total dos negativos = {somaN}")
