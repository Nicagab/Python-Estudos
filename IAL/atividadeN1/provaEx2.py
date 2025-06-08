a = True
while a:
    n = input().split()  

    H = float(n[0])
    C = float(n[1])
    L = float(n[2])

    if H == 0 and L == 0 and C == 0:
        print("Fim do Programa")
        a = False
    else: 
        i = H * 100 / C

        if i <= 8.334 and L > 0.8:
            print("PROJETO SIMPLES")
        else:
            print("PROJETO ESPECIAL")
