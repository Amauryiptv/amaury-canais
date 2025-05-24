import os
import requests
from urllib.parse import urlparse, parse_qs

PASTA = "/storage/emulated/0/Hits"
ARQUIVO_SAIDA = os.path.join(PASTA, "analise.txt")

def criar_pasta():
    if not os.path.exists(PASTA):
        os.makedirs(PASTA)

def limpar():
    os.system("clear" if os.name == "posix" else "cls")

def salvar_analise(texto):
    with open(ARQUIVO_SAIDA, "w", encoding="utf-8") as f:
        f.write(texto)

def extrair_dados(link):
    parsed = urlparse(link)
    query = parse_qs(parsed.query)
    usuario = query.get("username", [""])[0]
    senha = query.get("password", [""])[0]
    servidor = f"{parsed.scheme}://{parsed.hostname}"
    porta = parsed.port if parsed.port else 80
    return servidor, porta, usuario, senha

def verificar_painel(servidor, porta, usuario, senha):
    url_api = f"{servidor}:{porta}/player_api.php?username={usuario}&password={senha}"
    try:
        r = requests.get(url_api, timeout=10)
        dados = r.json()
        if "user_info" in dados:
            status = dados["user_info"]["status"]
            expira = dados["user_info"].get("exp_date", "Desconhecida")
            lista_canais = dados.get("available_channels", [])
            categorias = dados.get("user_info", {}).get("allowed_output_formats", [])
            return status, expira, categorias
        else:
            return "Desconhecido", "?", []
    except:
        return "Erro", "?", []

def buscar_dns_alternativas(servidor):
    try:
        ip = servidor.replace("http://", "").replace("https://", "")
        r = requests.get(f"https://
