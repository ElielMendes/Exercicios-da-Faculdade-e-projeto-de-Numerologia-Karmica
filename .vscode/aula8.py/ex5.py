import math

num = int(input('Digite um número: '))

while num > 0:
    print(f'\nNúmero digitado: {num}')
    quadrado = math.pow(num, 2)
    print(f'O quadrado é: {quadrado}')
    cubo = math.pow(num, 3)
    print(f'O cubo é: {cubo}')
    raiz = math.sqrt(num)
    print(f'A raíz quadrada é: {raiz:.1f}')

    num = int(input('\nDigite um número: '))

