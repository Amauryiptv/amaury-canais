# m3u_all_in_one_qpython.py
# Analisador completo de link M3U
# Compatível com QPython (Android)
# Uso educacional / listas autorizadas

import os
import re
import sys
import urllib.request
from urllib.parse import urlparse
from datetime import datetime

PASTA = "/storage/emulated/0/Hits"

PAINEIS_TESTE = [
    "/player_api.php",
    "/panel_api.php",
    "/xui",
    "/dashboard",
    "/panel"
]

def criar_pasta():
    if not os.path.exists(PASTA):
        os.makedirs(PASTA)

def banner():
    print("=" * 70)
    print("   ANALISADOR M3U ALL-IN-ONE  |  PYTHON ANDROID")
    print("=" * 70)

def baixar_m3u(url):
    try:
        req = urllib.request.Request(
            url,
            headers={"User-Agent": "Mozilla/5.0"}
        )
        with urllib.request.urlopen(req, timeout=20) as r:
            return r.read().decode("utf-8", errors="ignore")
    except Exception as e:
        print("❌ Erro ao baixar M3U:", e)
        return None

def validar_m3u(texto):
    return texto.strip().startswith("#EXTM3U")

def detectar_xtream(texto):
    padrao = r'(http[s]?://[^/]+)/get\\.php\\?username=([^&]+)&password=([^&]+)'
    m = re.search(padrao, texto)
    if m:
        return {
            "servidor": m.group(1),
            "usuario": m.group(2),
            "senha": m.group(3)
        }
    return None

def servidores_origem(texto):
    urls = re.findall(r'http[s]?://[^\\s"]+', texto)
    dominios = set()
    for u in urls:
        try:
            dominios.add(urlparse(u).netloc)
        except:
            pass
    return sorted(dominios)

def contar_conteudo(texto):
    live = texto.lower().count("/live/")
    movie = texto.lower().count("/movie/")
    series = texto.lower().count("/series/")
    return live, movie, series

def testar_painel(base):
    ativos = []
    for p in PAINEIS_TESTE:
        try:
            url = base + p
            req = urllib.request.Request(
                url,
                headers={"User-Agent": "Mozilla/5.0"}
            )
            with urllib.request.urlopen(req, timeout=6) as r:
                if r.status in (200, 401):
                    ativos.append(p)
        except:
            pass
    return ativos

def gerar_relatorio(url, texto):
    criar_pasta()
    agora = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    arquivo = f"{PASTA}/relatorio_m3u_{agora}.txt"

    xtream = detectar_xtream(texto)
    servidores = servidores_origem(texto)
    live, movie, series = contar_conteudo(texto)

    with open(arquivo, "w", encoding="utf-8") as f:
        f.write("RELATÓRIO COMPLETO DE LINK M3U\n")
        f.write("=" * 55 + "\n\n")
        f.write(f"URL ANALISADA:\n{url}\n\n")
        f.write("VALIDAÇÃO:\nLista M3U válida\n\n")

        if xtream:
            f.write("XTREAM CODES DETECTADO:\n")
            f.write(f"Servidor: {xtream['servidor']}\n")
            f.write(f"Usuário : {xtream['usuario']}\n")
            f.write(f"Senha  : {xtream['senha']}\n\n")

            paineis = testar_painel(xtream["servidor"])
            if paineis:
                f.write("PAINEL DE ORIGEM PROVÁVEL:\n")
                for p in paineis:
                    f.write(f"- {xtream['servidor']}{p}\n")
                f.write("\n")
            else:
                f.write("PAINEL DE ORIGEM:\nNão identificado\n\n")
        else:
            f.write("XTREAM CODES:\nNão detectado\n\n")

        f.write("SERVIDORES / DOMÍNIOS ENCONTRADOS:\n")
        for s in servidores:
            f.write(f"- {s}\n")
        f.write("\n")

        f.write("CONTEÚDO IDENTIFICADO (estimativa):\n")
        f.write(f"Live   : {live}\n")
        f.write(f"Movies : {movie}\n")
        f.write(f"Series : {series}\n\n")

        f.write("Status: Análise concluída com sucesso.\n")

    return arquivo

def main():
    banner()
    url = input("\nCole a URL M3U: ").strip()

    print("\n⬇️ Baixando lista...")
    texto = baixar_m3u(url)

    if not texto:
        sys.exit()

    if not validar_m3u(texto):
        print("❌ Lista inválida")
        sys.exit()

    print("✅ Lista válida")
    print("🔎 Analisando...")

    caminho = gerar_relatorio(url, texto)

    print("\n✔️ FINALIZADO")
    print("📁 Relatório salvo em:")
    print(caminho)

if __name__ == "__main__":
    main()
