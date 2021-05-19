# inicializa os contadores

# estrutura do for
    # leitura da idade altura e peso
    # condicoes (if)
    # 

acm_idade = 0
acm_peso = 0
acm_altura = 0
cont_altura = 0


for cont in range(1,25):
    idade = int(input(f'Digite a idade da {cont}ª pessoa: '))
       
    altura = float(input(f'Digite a altura da {cont}ª pessoa: '))
        
    peso = int(input(f'Digite o peso da {cont}ª pessoa: ')) 
    
    if idade > 50:
        acm_idade += 1
    if idade >= 10 and idade <= 20:
        acm_altura += altura
        cont_altura += 1
    if peso < 40:
        acm_peso += 1

print(f'{acm_idade} pessoas tem mais de 50 anos. ')
if cont_altura > 0:
    media_altura = acm_altura / cont_altura
else:
    meida_altura = 0
print(f'a médias das alturas das pessoas com idade entre 10 e 20 anos é de {media_altura}')
print(f'a porcentagem de pessoas com peso inferior a 40 kg é de {(acm_peso*100)/25}')