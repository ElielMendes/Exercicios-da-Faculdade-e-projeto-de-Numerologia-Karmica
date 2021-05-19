print("calculadora")

n1 = float(input("digite o primeiro número: "))
n2 = float(input("digite o segundo número: "))

calculo = input("digite a operação desejada entre as seguintes opções: (x = Soma, y = Subtração, z = multiplicação e u = divisão ): ")

if (calculo!= "x" and calculo!="y" and calculo!="z" and calculo!="u"):
    print("Sinal Inválido")
elif calculo == "x":
    print("o resultado é " , (n1+n2))
elif calculo == "y":
    print("o resultado é " , (n1-n2))
elif calculo == "z":
    print("o resultado é " , (n1*n2))
elif calculo == "u":
    if n2==0:
        print("Impossível dividir!!")
    else:
        print("o resultado é " , (n1/n2))
