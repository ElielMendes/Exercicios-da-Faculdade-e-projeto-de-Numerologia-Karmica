print("vamos calcular o consumo de energia de uma residência")
salario = float(input("Digite o salário mínimo atual"))
quilowatt = salario / 500
gasto = float(input("digite quantos quilowatts foram gastos esse mes"))
desconto = (gasto * quilowatt) * (1-25/100)
print("o valor de cada quilowatt é R$" , quilowatt)
print("o valor a ser pago por essa redidência é R$ " , (gasto * quilowatt))
print("o valor a ser pago com desconto é de R$" , desconto)

