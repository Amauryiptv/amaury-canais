# m3u_profissional_qpython.py
# Analisador profissional de M3U por URL
# Compatível com QPython - Android
# Uso educacional / listas próprias

import re
import sys
import os
import urllib.request
from urllib.parse import urlparse
from datetime import datetime

PASTA_SAIDA = "/storage/emulated/0/Hits"

def criar_pasta():
    if not os.path.exists(PASTA_SAIDA):
        os.makedirs(PASTA_SAIDA)

def banner():
    print("=" * 65)
    print("      ANALISADOR PROFISSIONAL M3U - QPYTHON")
    print("      URL M3U → Relatório automático")
    print("=" * 65)

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

def extrair_xtream(texto):
    padrao = r'(http[s]?://[^/]+)/get\\.php\\?username=([^&]+)&password=([^&]+)'
    m = re.search(padrao, texto)
    if m:
        return m.group(1), m.group(2), m.group(3)
    return None

def descobrir_servidores(texto):
    urls = re.findall(r'http[s]?://[^\\s"]+', texto)
    servidores = set()
    for u in urls:
        try:
            servidores.add(urlparse(u).netloc)
        except:
            pass
    return sorted(servidores)

def contar_conteudo(texto):
    live = texto.lower().count("/live/")
    movie = texto.lower().count("/movie/")
    series = texto.lower().count("/series/")
    return live, movie, series

def gerar_relatorio(url, texto):
    criar_pasta()
    agora = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    arquivo = f"{PASTA_SAIDA}/resultado_m3u_{agora}.txt"

    servidores = descobrir_servidores(texto)
    xtream = extrair_xtream(texto)
    live, movie, series = contar_conteudo(texto)

    with open(arquivo, "w", encoding="utf-8") as f:
        f.write("ANÁLISE PROFISSIONAL DE LISTA M3U\n")
        f.write("=" * 50 + "\n\n")
        f.write(f"URL ANALISADA:\n{url}\n\n")

        f.write("VALIDAÇÃO:\n")
        f.write("Lista M3U válida\n\n")

        if xtream:
            f.write("DADOS XTREAM CODES:\n")
            f.write(f"Servidor: {xtream[0]}\n")
            f.write(f"Usuário : {xtream[1]}\n")
            f.write(f"Senha  : {xtream[2]}\n\n")
        else:
            f.write("DADOS XTREAM CODES:\nNão detectado\n\n")

        f.write("SERVIDORES DE ORIGEM ENCONTRADOS:\n")
        for s in servidores:
            f.write(f"- {s}\n")
        f.write("\n")

        f.write("CONTEÚDO IDENTIFICADO (estimativa):\n")
        f.write(f"Live   : {live}\n")
        f.write(f"Movies : {movie}\n")
        f.write(f"Series : {series}\n\n")

        f.write("Relatório gerado com sucesso.\n")

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

    print("✅ Lista M3U válida")
    print("📄 Gerando relatório...")

    caminho = gerar_relatorio(url, texto)

    print("\n✔️ Análise concluída!")
    print("📁 Arquivo salvo em:")
    print(caminho)

if __name__ == "__main__":
    main()
