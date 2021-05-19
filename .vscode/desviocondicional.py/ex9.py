print("""

Uma prova possui 5 questões de múltipla escolha, onde cada uma possui 4 opções distintas. 
De quantas maneiras a prova pode ser resolvida?
(a)512
(b)1024
(c)525
(d)2056
(e)520

""")

resposta = str(input("digite sua resposta (a,b,c,d ou e): "))

if resposta == "b":
    print("a resposta marcada é (b)")
    print("você acertou")
elif resposta == "a":
    print("a resposta marcada é (a)")
    print("resposta errada")
elif resposta == "d":
    print("a resposta marcada é (d)")
    print("resposta errada")
elif resposta == "c":
    print("a resposta marcada é (c)")
    print("resposta errada")
elif resposta == "e":
    print("a resposta marcada é (e)")
    print("resposta errada")
else:
    print("não confere")