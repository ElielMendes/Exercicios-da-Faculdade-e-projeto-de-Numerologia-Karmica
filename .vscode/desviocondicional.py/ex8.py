mesada = float(input("digite o valor de sua mesada: "))
produto = str(input("deseja comprar um produto? (S = sim / N = não): "))

if produto == "S":
    valor_produto = float(input("digite o valor do produto: "))
    if valor_produto - mesada <= 0:
        print(f"seu saldo é de R$ {mesada - valor_produto}")
    else:
        print("saldo insuficiente")
else:
    print(f"seu saldo é de R$ {mesada}")