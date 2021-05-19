valor_cachorroquente = 0
valor_baurusimples = 0
valor_baurucomovo = 0
valor_hamburguer = 0
valor_cheeseburguer = 0
valor_refrigerante = 0



while True:
    while True:
        cod_produto = int(input("Digite o código do produto que deseja comprar: "))
        if cod_produto < 100 or cod_produto > 105:
            print("===>Erro: código inválido. o código deve ser de 100 a 105")
        else:
            break
    qt_produto = int(input("Digite quantas unidades deseja desse produto: "))
    mais_produtos = str(input("Deseja comprar mais produtos(S/N) ? ")).lower()
    if cod_produto == 100:
        valor_cachorroquente = qt_produto * 1.20
        qt_cachorroquente = qt_produto
    if cod_produto == 101:
        valor_baurusimples = qt_produto * 1.30
        qt_baurusimples = qt_produto
    if cod_produto == 102:
        valor_baurucomovo = qt_produto * 1.50
        qt_baurucomovo = qt_produto
    if cod_produto == 103:
        valor_hamburguer = qt_produto * 1.20
        qt_hamburguer = qt_produto
    if cod_produto == 104:
        valor_cheeseburguer = qt_produto * 1.30
        qt_cheeseburguer = qt_produto
    if cod_produto == 105:
        valor_refrigerante = qt_produto *  1.00
        qt_refrigerante = qt_produto
    if mais_produtos == "N":
        break

if valor_cachorroquente > 0:
    print(f"a quantidade de cachorro(s) quente(s) é de {qt_cachorroquente} com o valor de R$ {valor_cachorroquente}")
if valor_baurusimples > 0:
    print(f"a quantidade de bauru simple(s) é de {qt_baurusimples} com o valor de R$ {valor_baurusimples}")
if valor_baurucomovo > 0:
    print(f"a quantidade de bauru com ovo é de {qt_baurucomovo} com o valor de R$ {valor_baurucomovo}")
if valor_hamburguer > 0:
    print(f"a quantidade de hamburguer(s) é de {qt_hamburguer} com o valor de R$ {valor_hamburguer}")
if valor_cheeseburguer > 0:
    print(f"a quantidade de cheseburguer(s) é de {qt_cheeseburguer} com o valor de R$ {valor_cheeseburguer}")
if valor_refrigerante > 0:
    print(f"a quantidade de refrigerante(s) é de {qt_refrigerante} com o valor de R$ {valor_refrigerante}")

print(f"o Valor Total é de R$ {valor_cachorroquente + valor_baurusimples + valor_baurucomovo + valor_hamburguer + valor_cheeseburguer +valor_refrigerante}")