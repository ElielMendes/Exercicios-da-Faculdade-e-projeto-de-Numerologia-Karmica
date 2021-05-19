palavras = []

for i in range(5):
     palavra = input(f'Digite a {i+1}a palavra: ')
     palavras.append(palavra)

# forma 1
tam = len(palavras)
for i in range(tam-1, -1, -1):
     print(palavras[i])

print()
# forma 2
for i in range(5):
     print(palavras[4 - i])
