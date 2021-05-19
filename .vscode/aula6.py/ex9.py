cont = 0
acm_nota1 = 0
acm_nota2 = 0

while cont < 5:
    while True:
        n1 = float(input(f"Digite a 1ª nota do {cont+1}ª aluno: "))
        acm_nota1 += n1
        if n1 < 0 or n1 > 10:
            print("==>Erro. nota inválida. digite entre 0 e 10.")
        else:
            break

    while True:
        n2 = float(input(f"Digite a 2ª nota do {cont+1}ª aluno: "))
        acm_nota2 += n2
        if n2 < 0 or n2 > 10:
            print("==>Erro. nota inválida. digite entre 0 e 10.")
        else:    
            break

    media_aluno = (n1 + n2) / 2
    print(f"a média do {cont+1}ª aluno é de {media_aluno}")
    
    cont = cont + 1
    
acm_nota = (acm_nota1 + acm_nota2) / cont
media_classe = acm_nota / 2
print(f"a média da classe é de {media_classe}")