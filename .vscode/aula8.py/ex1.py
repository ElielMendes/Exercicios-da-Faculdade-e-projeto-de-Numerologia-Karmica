quant_pessoas = 0
quant_pessoas1 = 0
quant_pessoas2 = 0


for cont in range(1,21):
    print(f'======= Digite os dados da {cont}ª pessoa =======')
    idade = int(input('Digite a idade: '))
    peso = float(input('Digite o peso: '))
    altura = float(input('Digite a altura: '))
    while True:
        cor_olhos = str(input('Digite a cor dos olhos (azul, preto, verde e castanho): ')).lower()
        if cor_olhos != 'azul' and cor_olhos != 'preto' and cor_olhos != 'verde' and cor_olhos != 'castanho':
            print('cor inválida, digite novamente')
        else:
            break
    if idade > 50 and peso < 60:
        quant_pessoas += cont
    if cor_olhos == 'azul':
        quant_pessoas1 += cont
        olhos_azuis = (quant_pessoas1 * 100) / 20
    if altura > 1.68 and cor_olhos != 'verde':
        quant_pessoas2 += cont

print(f'A quantidade de pessoas com idade superior a 50 anos e peso inferior a 60 quilos é de {quant_pessoas}')
print(f'{olhos_azuis:.1f}% das pessoas tem olhos azuis')
print(f'A quantidade de pessoas com altura acima de 1,68 m e que não possuem olhos verdes é de: {quant_pessoas2}')
