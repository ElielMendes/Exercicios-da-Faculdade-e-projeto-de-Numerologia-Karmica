print("Gratificação")
numero_horas_extras = float(input("Digite a quantidade de horas extras realizadas: "))
numero_faltas = float(input("Digite o número de faltas ocorridas: "))

H = numero_horas_extras - (2/3 * numero_faltas)

if H >= 2400:
    print("prêmio de R$ 500,00")
elif H > 1800 and H < 2400:
    print("prêmio de R$ 400,00")
elif H >= 1200 and H < 1800:
    print("prêmio de R$ 300,00")
elif H >= 600 and H < 1200:
    print("prêmio de R$ 200,00")
elif H < 600:
    print("prêmio de R$ 100,00")
