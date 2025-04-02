nums = []
num = int(input("Insira um número: "))

while num>0:
    nums.append(num)
    num = int(input("Insira um número: "))

i = 0

while i<len(nums):
    print(nums[i])
    i += 1