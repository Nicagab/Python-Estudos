num = int(input("Digite um número: "))
nums = ""
arquivo = open("ex005.txt", "w")

while num!=0:
    if num%2==0 and num%3==0:
        nums += f"{num},"
    arquivo.write(f"Números digitados divisiveis por 2 e 3: {nums}\n")
    print(f"Números digitados divisiveis por 2 e 3: {nums}")
    num = int(input("Digite um número: "))

arquivo.close()
