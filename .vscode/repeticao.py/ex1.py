n1 = int(input("Digite um número inteiro: "))
n2 = int(input("Digite outro número inteiro: "))
cont = n1
qt_impares = 0


while cont <= n2:
    
    if cont % 2 != 0:
       qt_impares += 1
    
    cont += 1
    

print(f"a quantidade de números impares é {qt_impares} ")

