lista_A = []
lista_B = []
lista_C = []

while True:
    n1 = int(input('Digite um número inteiro para a lista A: '))
    lista_A.append(n1)
    cond = input('Deseja continuar com a lista A ? (S/N): ')
    if cond.lower() == 'n':
        break

while True:
    n2 = int(input('Digite um número inteiro para a lista B: '))
    lista_B.append(n2)
    cond = input('Deseja continuar com a lista B ? (S/N): ').lower()
    if cond.lower() == 'n':
        break

for i in lista_C:
    lista_C.append(n1 - n2)

print(lista_C)
