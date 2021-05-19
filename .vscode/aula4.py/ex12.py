print("cálculo do INSS")

salario = float(input("digite o valor de seu salário bruto: "))

if salario<=600.00:
    print("isento")
elif salario>600.00 and salario<=1200.00:
    print("o desconto do INSS será de R$" , (salario*20/100))
elif salario>1200.00 and salario<=2000.00:
    print("o desconto do INSS será de R$ ", (salario*25/100))
elif salario>2000.00:
    print("o desconto do INSS será de R$ ", (salario*30/100))

print("cálculo encerrado")