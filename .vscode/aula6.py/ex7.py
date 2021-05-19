cont = 0
pessoas_magras = 0

while cont < 20:
    alt = float(input(f"Digite a altura da {cont + 1}ª pessoa: "))
    peso = float(input(f"Digite o peso da {cont + 1}ª pessoa: "))
    imc = peso / alt**2
    print(f"o IMC da {cont + 1} ª pessoa é de {imc}")
    cont = cont + 1
    
    if imc >= 18.5 and imc <= 24.9:
        pessoas_magras += 1


print(f"o número de pessoas sem obesidade é de {pessoas_magras}")

