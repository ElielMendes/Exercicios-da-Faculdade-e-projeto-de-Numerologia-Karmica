altura = float(input("digite sua altura "))
sexo = str(input("digite seu sexo (M ou F) "))

if sexo == "M":
    print("seu peso ideal é de" , (72.7*altura)-58)

else:
    print("seu peso ideal é de" , (62.1*altura)-44.7)

print("fim")

