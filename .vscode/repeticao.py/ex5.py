print("jogo de adivinhar um número")

import random
x = random.randint (0,100)

tentativa = 0

while True:
    n1 = int(input("Tente adivinhar o número: "))
    if n1 > x:
        print(f"{n1} é maior do que o número sorteado")
    if n1 < x:
        print(f"{n1} é menor do que número sorteado")    
    if n1 == x:
        break
    tentativa += 1 

print(f"Felicitações! você acertou, o número sorteado foi {x} e o número total de tentativas feitas foram {tentativa}")