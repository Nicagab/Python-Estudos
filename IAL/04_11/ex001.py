cont = 0
elementos = []
while cont<10:
    elemento = input("Digite um elemento:")
    elementos.append(elemento)
    cont += 1

i = 0

while i<10:
    print(f"{i+1}º elemento: {elementos[i]}")
    i += 1