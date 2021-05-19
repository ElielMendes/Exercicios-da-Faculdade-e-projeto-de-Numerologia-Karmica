media_altura = 0
acm_cont = 0

for cont in range(1,6):
    print(f'===============Digite os dados da {cont}ª pessoa:================')
    idade = int(input('Digite a idade: '))
    altura = float(input('Digite a altura: '))
    
    if idade > 50:
        media_altura += altura
        acm_cont += 1
    
    
print(f'a médias da altura das pessoas com mais de 50 anos é de {media_altura / acm_cont:.2f}')