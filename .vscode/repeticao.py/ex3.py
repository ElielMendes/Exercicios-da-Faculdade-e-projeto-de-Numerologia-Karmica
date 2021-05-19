
maior = 0
menor = 9999999999999999

while True:
    nota = int(input("Digite uma nota: "))
    if nota < menor and nota > 0:
        menor = nota

    if nota > maior:
        maior = nota

    if nota < 0:
        break

print(f"o maior número é {maior}")
print(f"o menor número é {menor}")