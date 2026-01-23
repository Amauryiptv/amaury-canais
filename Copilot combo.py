import random

# Lista ampliada de nomes brasileiros
nomes = [
    "joao", "jose", "antonio", "francisco", "carlos", "paulo", "pedro", "lucas",
    "marcos", "rafael", "gabriel", "rodrigo", "thiago", "bruno", "andre", "roberto",
    "fernando", "daniel", "vinicius", "gustavo", "maria", "ana", "juliana", "camila",
    "fernanda", "patricia", "aline", "carla", "marcia", "eliane", "claudia", "debora",
    "fabiana", "leticia", "renata", "simone", "talita", "vanessa", "beatriz", "luana"
]

# Lista de senhas fixas
senhas_base = [
    "123456", "12345678", "123456789", "102030", "10203040",
    "senha123", "brasil2024", "abcd1234", "qwerty", "000000",
    "111111", "123123"
]

combos = []

# Gera combinações fixas
for nome in nomes:
    for senha in senhas_base:
        combos.append(f"{nome}:{senha}")
    combos.append(f"{nome}:{nome}")
    combos.append(f"{nome}:{nome}123")
    combos.append(f"{nome}:{nome}2025")

# Gera variações aleatórias até chegar em 10.000 combinações
while len(combos) < 10000:
    nome = random.choice(nomes)
    numero = random.randint(1000, 9999)
    combos.append(f"{nome}:{nome}{numero}")

# Salva no arquivo combo.txt
with open("combo.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(combos))

print("combo.txt com 10.000 combinações gerado com sucesso!")
