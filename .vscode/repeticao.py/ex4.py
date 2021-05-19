cont = 0
baixo = 0

while cont < 5:
    nome = str(input(f"Digite o nome do {cont+1}ª jogador: "))
    altura = float(input(f"Digite a altura do {cont+1}ª jogador: "))
    
    if cont == 0:
        baixo = altura
    
    if altura < baixo:
        baixo = altura
        nome_baixo = nome
    cont += 1 

print(f"o jogador mais baixo é {nome_baixo} com altura de {baixo} metros.")