fib = "0,1"

num = int(input("Digite um número: "))
i = 0
ult = 1
pen = 0
penC = 0
while i<num-2:
    fib += f",{ult+pen}"
    pen = ult
    ult = ult+penC
    penC = pen
    i +=1

arquivo = open("ex009.txt", "w")
arquivo.write(f"{fib}")
arquivo.close()
print(fib)
