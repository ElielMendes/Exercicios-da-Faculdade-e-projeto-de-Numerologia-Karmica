dividendo = float(input("Digite um número: "))
cociente = dividendo/2
resto = dividendo%2

if resto == 0 and dividendo > 0:
    print("o número é par e positivo")
else:
    print("o número não é par ou positivo")

