peso_saco = float(input('saco em kg: '))
qtd_racao1 = int(input('quantidade em gramas: '))
qtd_racao2 = int(input('quantidade em gramas: '))
X = peso_saco - ((qtd_racao1/1000) + (qtd_racao2/1000))*5
print(f'Sobraram {X:.2f} quilos de ração no saco')

