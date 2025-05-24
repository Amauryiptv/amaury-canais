import os
import requests
import hashlib
from datetime import datetime

# === Configurações ===
url = "http://SEULINK.com:porta/panel.php"  # Substitua pelo link real do painel IPTV
pasta_logs = "/storage/emulated/0/Download/Hits/painel_logs"
arquivo_hash = os.path.join(pasta_logs, "hash_anterior.txt")

# Cria a pasta se não existir
os.makedirs(pasta_logs, exist_ok=True)

try:
    r = requests.get(url, timeout=10)
    r.raise_for_status()
    html = r.text
except Exception as e:
    print("[ERRO] Não foi possível acessar o painel:")
    print(e)
    exit()

# Gera o hash do conteúdo HTML atual
hash_atual = hashlib.md5(html.encode("utf-8")).hexdigest()

# Lê o hash anterior, se existir
hash_antigo = ""
if os.path.exists(arquivo_hash):
    with open(arquivo_hash, "r") as f:
        hash_antigo = f.read().strip()

# Compara hashes para detectar mudanças
if hash_atual != hash_antigo:
    print("[!] MUDANÇA DETECTADA NO PAINEL!")
    data = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    nome_arquivo = f"painel_{data}.html"
    caminho_arquivo = os.path.join(pasta_logs, nome_arquivo)

    # Salva o conteúdo novo
    with open(caminho_arquivo, "w", encoding="utf-8") as f:
        f.write(html)

    # Atualiza o hash salvo
    with open(arquivo_hash, "w") as f:
        f.write(hash_atual)

    print(f"[+] Conteúdo salvo em: {caminho_arquivo}")
else:
    print("[=] Nenhuma mudança detectada no painel.")
