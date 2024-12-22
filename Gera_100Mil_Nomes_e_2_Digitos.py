from faker import Faker
import random

fake = Faker('pt_BR')

def gerar_usuarios_e_senhas(qtd):
    usuarios_senhas = []

    for _ in range(qtd):
        nome = fake.first_name().lower()  # Nome em minúsculas
        digito = str(random.randint(0,9)).zfill(1)  # Gera um número de dois dígitos
        usuario = f"{nome}"
        senha = usuario  # Senha igual ao usuário
        usuarios_senhas.append(f"{usuario}:{senha}")

    return usuarios_senhas

# Gera 100.000 mil usuários e senhas
usuarios_senhas = gerar_usuarios_e_senhas(100000)
print("Gerando Arquivo.")

# Salva em um arquivo
with open("/sdcard/combo/usuarios_senhas1.txt", "w") as f:
    for usuario_senha in usuarios_senhas:
        f.write(usuario_senha + "\n")

print("Arquivo gerado com 100000 mil usuários e senhas.")
