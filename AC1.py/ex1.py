qtd_min = int(input('Digite a quantidade mínima necessária em estoque do produto: '))
qtd_max = int(input('Digite a quantidade máxima que um produto pode ocupar no estoque: '))
qtd_atual = int(input('Digite a quantidade atual em estoque do produto: '))
qtd_media = (qtd_max + qtd_min) / 2

if qtd_atual >= qtd_media:
    print('Não efetuar compra')
else:
    print('Efetuar compra')
