n1 = int(input("Digite um número inteiro: "))
cont = 1
nr_str = ""

while cont < n1:
    if cont == 1:
        nr_str = str(cont) 
    cont = cont * 2 
    if cont < n1: 
        nr_str = nr_str + ", " + str(cont) 

print(nr_str)
