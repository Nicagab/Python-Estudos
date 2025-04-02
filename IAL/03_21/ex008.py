num = int(input("Digite um número: "))
arquivo = open("ex008.txt", "w")

i = 2
resp = "Este número é primo"

while i<num:
    if num%i==0:
        resp = "Este número não é primo"
    i += 1

arquivo.write(resp)
arquivo.close()
print(resp)
