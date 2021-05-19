print("Saiba o seu Bônus")
salario = float(input("digite o valor do seu salário"))
tempo = int(input("digite quantos anos ja trabalhou na empresa"))

if tempo >= 5:
    print("Seu bônus será de R$" , (salario*20/100))

else:
    print("seu bônus será de R$" , (salario*10/100))

print("fim")

