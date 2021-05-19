print("Linha de Crédito para Estatuários")
salario = float(input("Digite o valor do seu salário bruto: "))
emprestimo = float(input("Digite o valor de empréstimo desejado: "))
numero_prest = float(input("Deseja parcelar em quantas prestações? "))
prestacao = emprestimo/numero_prest

print("Salário Bruto: " , (salario))
print("Valor da prestação: R$ " , (prestacao))

if prestacao <= salario*30/100:
    print("empréstimo concedido")

else:
    print("empréstimo não pode ser concedido")

print("processo encerrado")