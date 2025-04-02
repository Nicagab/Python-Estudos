num = int(input("Digite um número:"))

i = 0
arquivo = open("ex001.txt", "a")

while i<=10:
    arquivo.write(f"{num} X {i} = {num*i}\n")
    print(f"{num} X {i} = {num*i}")
    i += 1

arquivo.close()
