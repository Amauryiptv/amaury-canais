# m3u_analisador_completo_qpython.py
# Analisador completo de M3U para QPython (Android)
# Uso educacional – listas próprias

import re
import sys
from urllib.parse import urlparse

def banner():
    print("=" * 55)
    print("      ANALISADOR COMPLETO M3U - QPYTHON")
    print("      Python no celular (terminal)")
    print("=" * 55)

def menu():
    print("\nEscolha uma opção:")
    print("1 - Analisar lista M3U")
    print("2 - Descobrir servidor de origem")
    print("3 - Analisar tudo (completo)")
    print("0 - Sair")

def ler_m3u():
    print("\nCole sua lista M3U abaixo.")
    print("Quando terminar, digite apenas: FIM")
    print("-" * 55)
    linhas = []
    while True:
        try:
            linha = input()
        except EOFError:
            break
        if linha.strip().upper() == "FIM":
            break
        linhas.append(linha)
    return "\n".join(linhas)

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
    print("-" * 55)

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

        elif opcao == "1":
            texto = ler_m3u()
            print("\n🔎 Verificando M3U...")
            if validar_m3u(texto):
                print("✅ Lista M3U válida")
            else:
                print("❌ Lista inválida")

        elif opcao == "2":
            texto = ler_m3u()
            servidores = descobrir_servidores(texto)
            print("\n🌐 Servidores de origem encontrados:")
            if servidores:
                for s in servidores:
                    print("-", s)
            else:
                print("Nenhum servidor identificado")

        elif opcao == "3":
            texto = ler_m3u()
            analisar_m3u(texto)

        else:
            print("\n❌ Opção inválida")

if __name__ == "__main__":
    main()
