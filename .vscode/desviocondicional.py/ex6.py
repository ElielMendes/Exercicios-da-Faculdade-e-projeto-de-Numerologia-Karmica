custo_produto = float(input("digite o valor de custo do produto:  "))

if custo_produto < 20:
    print(f"o valor de venda será de R$ {custo_produto + (custo_produto*0.45)}")
else:
    print(f"o valor de venda será de R$ {custo_produto + (custo_produto*0.30)}")