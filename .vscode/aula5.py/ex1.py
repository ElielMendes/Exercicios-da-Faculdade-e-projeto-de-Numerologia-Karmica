print("média de notas")

n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))
media = (n1+n2+n3)/3

print(f"sua média é : {media:.2f}")

if (media >= 0 and media < 3):
    print("reprovado")
elif (media >= 3 and media < 6):
    print("exame")
    print(f"necessário tirar {12-media:.2f}")
elif (media >= 6 and media <= 10):
    print("aprovado")

