min = int(input("Valor mínimo:"))
max = int(input("Valor máximo:"))
arquivo = open("ex002.txt", "w")

while min>=max:
    print("O valor mínimo não pode ser maior que o máximo")
    min = int(input("Valor mínimo:"))
    max = int(input("Valor máximo:"))

i = min+1
nums = []

while i<max:
    if i%5==0:
        nums.append(i)
    i += 1

arquivo.write(f"{nums}")
print(f"{nums}")
arquivo.close()
