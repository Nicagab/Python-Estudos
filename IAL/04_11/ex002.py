cont = 0
elementos = []
while cont<10:
    elemento = input("Digite um elemento:")
    elementos.append(elemento)
    cont += 1

i = 10

while i!=0:
    print(f"{i}º elemento: {elementos[i-1]}")
    i += -1