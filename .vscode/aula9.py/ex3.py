lista_A = []
lista_B = []

for i in range(8):
    num = int(input(f'Digite o {i+1}ª numero: '))
    lista_A.append(num)  

print(lista_A)

for num in lista_A:
    lista_B.append(num*3)

print(lista_B)