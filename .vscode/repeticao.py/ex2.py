import random
y = int(input("Digite um número inteiro: "))

while True:
    x = random.randint (1,10)
    z = random.randint (1,10)
    if x + z == y:
        break

print(f"a soma é {x} + {z} = {y}")