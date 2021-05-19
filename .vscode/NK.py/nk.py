# Numerologia Kármica
pi = int(input("Digite o dia do seu nascimento: "))
pe = int(input("Digite o mês do seu nascimento: "))
ano = int(input("Digite o ano do seu nascimento: "))
soma_pi = 0
soma_pe = 0
soma_ano = 0

if pi > 22:
    pi_str = str(pi)
    for i in pi_str:
        soma_pi += int(i)
else:
    soma_pi = pi

print(f"a personalidade interna é {soma_pi}")

# ------------------------------------------------

if pe > 22:
    pe_str = str(pe)
    for i in pe_str:
        soma_pe += int(i)
else:
    soma_pe = pe

print(f"a personalidade externa é {soma_pe}")

# --------------------------------------------------

ano_str = str(ano)
for i in ano_str:
    soma_ano += int(i)
if soma_ano > 22:
    ano_str = str(soma_ano)
    soma_ano = 0
    for i in ano_str:
        soma_ano += int(i)
print(f"a regência de vida anterior é {soma_ano}")

# --------------------------------------------------

mva = pi + pe + ano
soma_mva = 0

if mva > 22:
    mva_str = str(mva)
    for i in mva_str:
        soma_mva += int(i)
    if soma_mva > 22:
        mva_str = str(soma_mva)
        soma_mva = 0
        for i in mva_str:
            soma_mva += int(i)
else:
    soma_mva = mva

print(f"a missão de vida atual é {soma_mva}")

# --------------------------------------------------

liberacao_karma = soma_pi + soma_pe + soma_ano + soma_mva
print(f"a liberação de karma será entre os {liberacao_karma - 2} e {liberacao_karma + 2 } anos")

# --------------------------------------------------

pg = soma_pi + soma_pe
soma_pg = 0

if pg > 22:
    pg_str = str(pg)
    for i in pg_str:
        soma_pg += int(i)
else:
    soma_pg = pg

print(f"a personalidade geral é {soma_pg}")

# --------------------------------------------------

po_str = str(soma_pg)
soma_po = 0

for i in po_str:
    soma_po = abs(soma_po - int(i))

print(f"a personalidade oculta é {soma_po}")

# --------------------------------------------------

df_str = str(soma_pg)
soma_df = 0

for i in df_str:
    soma_df = soma_df + int(i)

print(f"o desafio é {soma_df}")

# --------------------------------------------------

arc_rva = soma_ano + soma_df
soma_arc_rva = 0

if arc_rva > 22:
    arc_rva_str = str(arc_rva)
    for i in arc_rva_str:
        soma_arc_rva += int(i)
else:
    soma_arc_rva = arc_rva

print(f"o arcano auxiliar da Regência de vida anterior é {soma_arc_rva}")

# --------------------------------------------------

arc_mva = soma_mva + soma_pg
soma_arc_mva = 0

if arc_mva > 22:
    arc_mva_str = str(arc_mva)
    for i in arc_mva_str:
        soma_arc_mva += int(i)
else:
    soma_arc_mva = arc_mva

print(f"o arcano auxiliar da Missão de vida atual é {soma_arc_mva}")

# --------------------------------------------------

ablo = soma_arc_rva + soma_arc_mva
soma_ablo = 0

if ablo > 22:
    ablo_str = str(ablo)
    for i in ablo_str:
        soma_ablo += int(i)
else:
    soma_ablo = ablo

print(f"o abalo de vida é {soma_ablo}")

# --------------------------------------------------

do = pi - pe
soma_do = 0

if do > 22:
    do_str = str(do)
    for i in do_str:
        soma_do += int(i)
else:
    soma_do = do

print(f"o desafio oculto é {soma_do}")




