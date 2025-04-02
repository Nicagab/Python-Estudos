p = int(input("Primeiro termo:"))
r = int(input("Razão da progressão:"))
n = int(input("Número de termos a ser mostrado:"))

i = 0

while i<n :
    print(p)
    p = p*r
    i = i+1

S = int(p*r**n-1)/(r-1)
print(f"Soma dos termos: {S}")
    
