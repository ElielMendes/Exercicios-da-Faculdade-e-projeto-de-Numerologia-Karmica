x = int(input("Digite um número inteiro: "))
y = int(input("Digite outro número inteiro: "))
z = int(input("Digite mais um número inteiro: "))

if (x == y and x == z and y == z and y ==x and z == x and z==y):
    print("os números são iguais")

else:
    if (x>y and x>z):
        print("o número maior é ", (x))
    elif (y>x and y>z):
        print("o número maior é ", (y))
    elif (z>x and z>y):
        print("o número maior é ", (z))

print("fim")
            
    