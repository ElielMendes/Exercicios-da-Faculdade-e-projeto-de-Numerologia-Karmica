aprovado = 0
exame = 0
reprovado = 0
acm_media = 0


for cont in range(1,7):
    print(f'----------Notas do {cont}ª aluno------------- ')
    n1 = float(input('Digite a 1ª nota: '))
    n2 = float(input('Digite a 2ª nota: '))
    media = (n1 + n2) / 2 
    acm_media += media
    
    if media < 3:
        reprovado += 1
        mensagem = 'REPROVADO'
    if media > 3 and media < 7:
        exame += 1 
        mensagem = 'EXAME'
    if media >= 7:
        aprovado += 1
        mensagem = 'APROVADO'
    print(f'A média de notas do {cont}ª aluno é: {media}. {mensagem} ')

print(f'Total de alunos reprovados: {reprovado}')
print(f'Total de alunos de exame: {exame}')
print(f'Total de alunos aprovados: {aprovado}')
print(f"A média da classe é: {acm_media / cont}")