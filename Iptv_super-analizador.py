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
            formatos = dados["user_info"].get("allowed_output_formats", [])
            return status, expira, formatos
        else:
            return "Desconhecido", "?", []
    except:
        return "Erro", "?", []

def buscar_dns_alternativas(servidor):
    try:
        ip = servidor.replace("http://", "").replace("https://", "")
        url = f"https://api.hackertarget.com/hostsearch/?q={ip}"
        r = requests.get(url, timeout=5)
        if r.status_code == 200 and ip not in r.text:
            return r.text.strip().splitlines()
        return []
    except:
        return []

def contar_categorias(link):
    try:
        r = requests.get(link, timeout=10)
        linhas = r.text.splitlines()
        canais, filmes, series = 0, 0, 0
        for l in linhas:
            if "#EXTINF" in l:
                l = l.lower()
                if "movie" in l:
                    filmes += 1
                elif "series" in l:
                    series += 1
                else:
                    canais += 1
        return canais, filmes, series
    except:
        return 0, 0, 0

def principal():
    criar_pasta()
    limpar()
    print("=== SUPER ANALISADOR IPTV ===")
    link = input("Cole o link M3U: ").strip()

    servidor, porta, usuario, senha = extrair_dados(link)
    status, expira, formatos = verificar_painel(servidor, porta, usuario, senha)
    canais, filmes, series = contar_categorias(link)
    alternativos = buscar_dns_alternativas(servidor)

    texto = f"""
========= RELATÓRIO IPTV =========

Servidor:   {servidor}
Porta:      {porta}
Usuário:    {usuario}
Senha:      {senha}
Status:     {status}
Expira em:  {expira}
Formatos:   {', '.join(formatos) if formatos else 'Desconhecido'}

Canais:     {canais}
Filmes:     {filmes}
Séries:     {series}

DNS Alternativos encontrados:
{chr(10).join(alternativos) if alternativos else 'Nenhum encontrado.'}

==================================
Relatório salvo em: {ARQUIVO_SAIDA}
"""

    print(texto)
    salvar_analise(texto)
    input("\nPressione Enter para sair...")

if __name__ == "__main__":
    principal()
