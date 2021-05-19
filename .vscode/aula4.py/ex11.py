print("Nadador, vamos identificar sua categoria!")
idade = int(input("Nadador, digite sua idade: "))

if idade<5:
    print("categoria: Bebê")
elif idade>=5 and idade<=7:
    print("categoria: Infantil A")
elif idade>=8 and idade<=10:
    print("categoria: Infantil B")
elif idade>=11 and idade<=13:
    print("categoria: Juvenil A")
elif idade>=14 and idade<=17:
    print("categoria: Juvenil B")
elif idade>=18:
    print("categoria: Sênior")

print("fim")