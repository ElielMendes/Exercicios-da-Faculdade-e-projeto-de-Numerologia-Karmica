print("carga do caminhão")

codigo_estado = int(input("digite o código de origem da carga (entre 1 a 5): "))
peso = float(input("digite o peso da carga em toneladas: "))
codigo_carga = int(input("digite o código da carga (entre 10 a 40): "))
peso_kg = peso*1000

print(f"o peso da carga é de {peso_kg} kg")

if codigo_carga>=10 and codigo_carga<=20 :
    print(f"o preço da carga é de R$ {peso_kg*100:,.2f}")
    if codigo_estado == 1:
        print(f"o valor do imposto é de R$ {(peso_kg*100)*0.35:,.2f}")
        print(f"o valor total da carga é de R$ {peso_kg*250 + ((peso_kg*100)*0.35):,.2f}")
    elif codigo_estado == 2:
        print(f"o valor do imposto é de R$ {(peso_kg*100)*0.25:,.2f}") 
        print(f"o valor total da carga é de R$ {peso_kg*250 + ((peso_kg*100)*0.25):,.2f}")
    elif codigo_estado == 3:
        print(f"o valor do imposto é de R$ {(peso_kg*100)*0.15:,.2f}")
        print(f"o valor total da carga é de R$ {peso_kg*250 + ((peso_kg*100)*0.15):,.2f}")
    elif codigo_estado == 4:
        print(f"o valor do imposto é de R$ {(peso_kg*100)*0.5:,.2f}")
        print(f"o valor total da carga é de R$ {peso_kg*250 + ((peso_kg*100)*0.05):,.2f}")
    elif codigo_estado == 5:
        print("isento de imposto")
        print(f"o valor total da carga é de R$ {peso_kg*100:,.2f}")
elif codigo_carga>=21 and codigo_carga<=30:
    print(f"o preço da carga é de R$ {peso_kg*250:,.2f}")
    if codigo_estado == 1:
        print(f"o valor do imposto é de R$ {(peso_kg*250)*0.35:,.2f}")
        print(f"o valor total da carga é de R$ {peso_kg*250 + ((peso_kg*250)*0.35):,.2f}")
    elif codigo_estado == 2:
        print(f"o valor do imposto é de R$ {(peso_kg*250)*0.25:,.2f}") 
        print(f"o valor total da carga é de R$ {peso_kg*250 + ((peso_kg*250)*0.25):,.2f}")
    elif codigo_estado == 3:
        print(f"o valor do imposto é de R$ {(peso_kg*250)*0.15:,.2f}")
        print(f"o valor total da carga é de R$ {peso_kg*250 + ((peso_kg*250)*0.15):,.2f}")
    elif codigo_estado == 4:
        print(f"o valor do imposto é de R$ {(peso_kg*250)*0.5:,.2f}")
        print(f"o valor total da carga é de R$ {peso_kg*250 + ((peso_kg*250)*0.05):,.2f}")
    elif codigo_estado == 5:
        print("isento de imposto")
        print(f"o valor total da carga é de R$ {peso_kg*250:,.2f}")
elif codigo_carga>=31 and codigo_carga<=40:
    print(f"o preço da carga é de R$ {peso_kg*340:,.2f}")
    if codigo_estado == 1:
        print(f"o valor do imposto é de R$ {(peso_kg*340)*0.35:,.2f}")
        print(f"o valor total da carga é de R$ {peso_kg*340 + ((peso_kg*340)*0.35):,.2f}")
    elif codigo_estado == 2:
        print(f"o valor do imposto é de R$ {(peso_kg*340)*0.25:,.2f}")
        print(f"o valor total da carga é de R$ {peso_kg*340 + ((peso_kg*340)*0.25):,.2f}") 
    elif codigo_estado == 3:
        print(f"o valor do imposto é de R$ {(peso_kg*340)*0.15:,.2f}")
        print(f"o valor total da carga é de R$ {peso_kg*340 + ((peso_kg*340)*0.15):,.2f}")
    elif codigo_estado == 4:
        print(f"o valor do imposto é de R$ {(peso_kg*340)*0.5:,.2f}")
        print(f"o valor total da carga é de R$ {peso_kg*340 + ((peso_kg*340)*0.05):,.2f}")
    elif codigo_estado == 5:
        print("isento de imposto")
        print(f"o valor total da carga é de R$ {peso_kg*340:,.2f}")