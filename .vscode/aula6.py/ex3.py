import random
cont = 0
par = 0
impar = 0

while cont < 200:
    x = random.randint (1,1000)
    if x % 2 == 0 :
        par = par + 1
    else:
        impar = impar + 1 
    cont = cont + 1

print(f"{par} são pares")
print(f"{impar} são impares")
print(f"total de {par + impar}")