import os
import requests
import hashlib
from datetime import datetime

# Link padrão que você pode alterar aqui:
link_padrao = "http://daxoi.online:80/get.php?username=Renataquarto&password=353620&type=m3u_plus"

print("=== Teste Painel IPTV ===")
print("1 - Usar link padrão")
print("2 - Digitar outro link")
escolha = input("Escolha opção (1 ou 2): ").strip()

if escolha == "1":
    url = link_padrao
else:
    url = input("Cole aqui o link do painel IPTV: ").strip()

pasta_logs = "/storage/emulated/0/Download/Hits/painel_logs"
arquivo_hash = os.path.join(pasta_logs, "hash_anterior.txt")

os.makedirs(pasta_logs, exist_ok=True)

try:
    r = requests.get(url, timeout=10)
    r.raise_for_status()
    html = r.text
except Exception as e:
    print("[ERRO] Não foi possível acessar o painel:")
    print(e)
    exit()

hash_atual = hashlib.md5(html.encode("utf-8")).hexdigest()

hash_antigo = ""
if os.path.exists(arquivo_hash):
    with open(arquivo_hash, "r") as f:
        hash_antigo = f.read().strip()

if hash_atual != hash_antigo:
    print("[!] MUDANÇA DETECTADA NO PAINEL!")
    data = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    nome_arquivo = f"painel_{data}.html"
    caminho_arquivo = os.path.join(pasta_logs, nome_arquivo)

    with open(caminho_arquivo, "w", encoding="utf-8") as f:
        f.write(html)

    with open(arquivo_hash, "w") as f:
        f.write(hash_atual)

    print(f"[+] Conteúdo salvo em: {caminho_arquivo}")
else:
    print("[=] Nenhuma mudança detectada no painel.")
