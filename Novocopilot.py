import random

# Lista de nomes (500 nomes, exemplo reduzido aqui)
nomes = ["joao","jose","maria","ana","lucas","camila","rafael","juliana"]

# Lista de senhas fixas
senhas_base = [
    "123456","12345678","123456789","102030","10203040",
    "senha123","brasil2024","abcd1234","qwerty","000000",
    "111111","123123"
]

# Usar um set para evitar duplicatas
combos = set()

# Gera combinações fixas
for nome in nomes:
    for senha in senhas_base:
        combos.add(f"{nome}:{senha}")
    combos.add(f"{nome}:{nome}")
    combos.add(f"{nome}:{nome}123")
    combos.add(f"{nome}:{nome}2025")

# Gera variações únicas até chegar em 100.000 combinações
while len(combos) < 100000:
    nome = random.choice(nomes)
    numero = random.randint(1000, 9999)
    combos.add(f"{nome}:{nome}{numero}")

# Salva no arquivo combo.txt
with open("combo.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(combos))

print("combo.txt com 100.000 combinações únicas gerado com sucesso!")
