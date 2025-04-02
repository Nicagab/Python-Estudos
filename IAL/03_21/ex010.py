fib = "0,1"

num = int(input("Digite um número: "))
prim = int(input("Digite um número: "))
i = 0
ult = 1
pen = 0
penC = 0
resp = ""
if pen>prim:
    resp += f"{pen},"
if ult>prim:
    resp += f"{ult},"
while i<num-2:
    fib += f",{ult+pen}"
    pen = ult
    ult = ult+penC
    penC = pen
    if ult>prim:
        resp += f"{ult},"
    i +=1

arquivo = open("ex009.txt", "w")
arquivo.write(resp)
arquivo.close()
print(resp)

