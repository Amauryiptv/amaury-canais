# m3u_analisador_link_qpython.py
# Analisador M3U por LINK para QPython (Android)
# Uso educacional – listas próprias

import re
import sys
import urllib.request
from urllib.parse import urlparse

def banner():
    print("=" * 60)
    print("   ANALISADOR M3U POR LINK - QPYTHON")
    print("   Python no celular (terminal)")
    print("=" * 60)

def menu():
    print("\nEscolha uma opção:")
    print("1 - Analisar link M3U")
    print("2 - Descobrir servidor de origem")
    print("3 - Analisar tudo (completo)")
    print("0 - Sair")

def baixar_m3u(url):
    try:
        req = urllib.request.Request(
            url,
            headers={"User-Agent": "Mozilla/5.0"}
        )
        with urllib.request.urlopen(req, timeout=15) as response:
            return response.read().decode("utf-8", errors="ignore")
    except Exception as e:
        print("❌ Erro ao baixar M3U:", e)
        return None

def validar_m3u(texto):
    return texto.strip().startswith("#EXTM3U")

def extrair_xtream(texto):
    padrao = r'(http[s]?://[^/]+)/get\\.php\\?username=([^&]+)&password=([^&]+)'
    match = re.search(padrao, texto)
    if match:
        return {
            "host": match.group(1),
            "usuario": match.group(2),
            "senha": match.group(3)
        }
    return None

def descobrir_servidores(texto):
    urls = re.findall(r'http[s]?://[^\\s"]+', texto)
    servidores = set()
    for url in urls:
        try:
            parsed = urlparse(url)
            servidores.add(parsed.netloc)
        except:
            pass
    return list(servidores)

def analisar_m3u(texto):
    print("\n🔍 RESULTADO DA ANÁLISE")
    print("-" * 60)

    if not validar_m3u(texto):
        print("❌ Lista inválida (não começa com #EXTM3U)")
        return

    print("✅ Lista M3U válida")

    xtream = extrair_xtream(texto)
    if xtream:
        print("\n📡 Dados Xtream Codes detectados:")
        print("Servidor :", xtream["host"])
        print("Usuário  :", xtream["usuario"])
        print("Senha   :", xtream["senha"])
    else:
        print("\nℹ️ Nenhum padrão Xtream Codes encontrado")

    servidores = descobrir_servidores(texto)
    if servidores:
        print("\n🌐 Servidores encontrados na lista:")
        for s in servidores:
            print("-", s)
    else:
        print("\nℹ️ Nenhum servidor identificado")

def main():
    banner()
    while True:
        menu()
        opcao = input("\nDigite a opção: ").strip()

        if opcao == "0":
            print("\nSaindo...")
            sys.exit()

        elif opcao in ("1", "2", "3"):
            link = input("\nCole o LINK M3U: ").strip()
            print("\n⬇️ Baixando lista M3U...")
            texto = baixar_m3u(link)

            if not texto:
                continue

            if opcao == "1":
                if validar_m3u(texto):
                    print("✅ Lista M3U válida")
                else:
                    print("❌ Lista inválida")

            elif opcao == "2":
                servidores = descobrir_servidores(texto)
                print("\n🌐 Servidores de origem encontrados:")
                if servidores:
                    for s in servidores:
                        print("-", s)
                else:
                    print("Nenhum servidor identificado")

            elif opcao == "3":
                analisar_m3u(texto)

        else:
            print("\n❌ Opção inválida")

if __name__ == "__main__":
    main()
