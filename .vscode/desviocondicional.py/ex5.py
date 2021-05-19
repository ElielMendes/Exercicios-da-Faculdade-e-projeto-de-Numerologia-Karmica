n1 = int(input("digite um número inteiro: "))

if (n1%10) == 0:
    print("número divisivel por 10 ")
elif (n1%5) == 0:
    print("número divisivel por 5 ")
elif (n1%2) == 0:
    print("número divisivel por 2 ")
else:
    print("número não divisivel por 10, 5 e 2")