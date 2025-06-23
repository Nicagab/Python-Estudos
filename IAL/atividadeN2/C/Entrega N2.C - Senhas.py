from random import randint

tipo = input("Tipo de senha: ")
tamanho = int(input("Tamanho da senha: "))

while tipo not in ["A","B","C","D","E"]:
    print("Tipo de senha inválido!")
    tipo = input("Tipo de senha: ")

while tamanho<6 or tamanho>25:
    print("Tamanho da senha inválido!")
    tamanho = int(input("Tamanho da senha: "))

def randAlgarismo():
    return str(randint(0,9))

def randMinuscula():
    return chr(randint(97, 122))

def randMaiuscula():
    return chr(randint(65, 90))

def randEspecial():
    especiais = ["+", "-", "_" , "!", "?", "#", "@", "*", "&", "=", "$", "%"]
    return especiais[randint(0,11)]

def gerarSenha(tipo, tam):
    senha = ""
    if tipo == "A":
        while len(senha)<tam:
            senha += randAlgarismo()
    elif tipo == "B":
        while len(senha)<tam:
            i = randint(1,2)
            if i == 1:
                senha += randMinuscula()
            else:
                senha += randMaiuscula()
    elif tipo == "C":
        while len(senha)<tam:
            i = randint(1,2)
            if i == 1:
                senha += randAlgarismo()
            else:
                senha += randMaiuscula()
    elif tipo == "D":
        while len(senha)<tam:
            i = randint(1,3)
            if i == 1:
                senha += randAlgarismo()
            elif i == 2:
                senha += randMinuscula()
            else:
                senha += randMaiuscula()
    elif tipo == "E":
        while len(senha)<tam:
            i = randint(1,4)
            if i == 1:
                senha += randAlgarismo()
            elif i == 2:
                senha += randMinuscula()
            elif i == 3:
                senha += randMaiuscula()
            else:
                senha += randEspecial()
    return senha

entrada = open('MATR.txt', "r")
saida = open('SENHAS.txt', "w")
matriculas = entrada.read().split("\n")

for matricula in matriculas:
    saida.write(f"{matricula};{gerarSenha(tipo, tamanho)};\n")


entrada.close()
saida.close()
