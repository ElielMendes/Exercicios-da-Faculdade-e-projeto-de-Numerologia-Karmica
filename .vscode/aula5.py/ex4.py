print("triangulo")

x = float(input("Digite o valor de X: "))
y = float(input("Digite o valor de y: "))
z = float(input("Digite o valor de z: "))

if (x==y and x==z and y==x and y==z and z==x and z==y):
    print("Triãngulo Equilátero")
elif (x!=y and x!=z and y!=x and y!=z and z!=x and z!=y):
    print("Triângulo Escaleno")
elif (y==z or x==z or y==x) and (x>=(y+z) or y>=(x+z) or z>=(x+y)):
    print("Triângulo Isósceles")
elif (x<(y+z) and y<(x+z) and z<(x+y)):
    print("não é um triãngulo")
