cont = 0
menor = 0

while cont < 10:
    n1 = int(input(f"Digite o {cont + 1}ª número inteiro: "))
    if cont == 0:
        menor = n1
    elif n1 < menor:
        menor = n1
    cont = cont + 1
    
print(f"o menor número é {menor}")