num = int(input("Digite um número: "))
soma = 0
arquivo = open("ex006.txt", "w")

if num<100:
    print("O número deve ser maior que 100!")
else:
    i = 1
    while i<num:
        if i%2==0:
            soma += i
        i += 1

arquivo.write(f"A soma de todos os números pares entre 1 e {num} é: {soma}")
arquivo.close()
print(f"A soma de todos os números pares entre 1 e {num} é: {soma}")
