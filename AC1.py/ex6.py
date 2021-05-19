while True:
    cod_cliente = int(input())
    if cod_cliente <= 0:
        break
    tipo_conta = int(input())
    valor_investido = float(input())
    if tipo_conta == 1:
        juros = valor_investido * 0.015
    if tipo_conta == 2:
        juros = valor_investido * 0.02
    if tipo_conta == 3:
        juros = valor_investido * 0.04
    print(f'Valor investido R$ {valor_investido:.2f} e Juros: R$ {juros:.2f}')