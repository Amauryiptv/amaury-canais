import os
import requests

PASTA = "/storage/emulated/0/Hits"
FAVORITOS_ARQ = os.path.join(PASTA, "favoritos.txt")

def criar_pasta():
    if not os.path.exists(PASTA):
        os.makedirs(PASTA)

def limpar():
    os.system("clear" if os.name == "posix" else "cls")

def abrir_no_player(url):
    try:
        cmd = f'am start -a android.intent.action.VIEW -d "{url}"'
        os.system(cmd)
    except Exception as e:
        print(f"Erro ao abrir: {e}")

def salvar_favorito(nome, url):
    with open(FAVORITOS_ARQ, "a") as f:
        f.write(f"{nome}|{url}\n")

def carregar_favoritos():
    if not os.path.exists(FAVORITOS_ARQ):
        return []
    with open(FAVORITOS_ARQ, "r") as f:
        return [linha.strip().split("|") for linha in f.readlines()]

def analisar_m3u(link):
    try:
        r = requests.get(link, timeout=10)
        r.raise_for_status()
        linhas = r.text.splitlines()
        tv, filmes, series = [], [], []

        for i in range(len(linhas)):
            if linhas[i].startswith("#EXTINF"):
                nome = linhas[i].split(",")[-1].strip()
                url = linhas[i + 1].strip() if i + 1 < len(linhas) else ""
                linha_lower = linhas[i].lower()

                if "movie" in linha_lower:
                    filmes.append((nome, url))
                elif "series" in linha_lower:
                    series.append((nome, url))
                else:
                    tv.append((nome, url))

        return tv, filmes, series
    except Exception as e:
        print(f"Erro ao baixar a lista: {e}")
        return [], [], []

def mostrar_lista(lista):
    for idx, (nome, _) in enumerate(lista):
        print(f"{idx+1}. {nome}")
    print("0. Voltar")

def menu_play(lista):
    while True:
        limpar()
        print("=== Lista de Itens ===")
        mostrar_lista(lista)
        escolha = input("\nEscolha um item: ")

        if escolha == "0":
            break
        try:
            idx = int(escolha) - 1
            nome, url = lista[idx]
            abrir_no_player(url)

            fav = input("Salvar nos favoritos? (s/n): ").lower()
            if fav == "s":
                salvar_favorito(nome, url)
                print("Salvo em favoritos!")
                input("Enter para continuar...")
        except:
            input("Opção inválida. Enter para tentar de novo...")

def menu_principal():
    limpar()
    print("=== IPTV Avançado com Favoritos ===")
    link = input("Cole o link M3U: ").strip()
    tv, filmes, series = analisar_m3u(link)

    while True:
        limpar()
        print("=== Escolha uma categoria ===")
        print(f"1. Canais ao Vivo ({len(tv)})")
        print(f"2. Filmes ({len(filmes)})")
        print(f"3. Séries ({len(series)})")
        print("4. Favoritos")
        print("0. Sair")

        op = input("\nDigite sua opção: ")
        if op == "1":
            menu_play(tv)
        elif op == "2":
            menu_play(filmes)
        elif op == "3":
            menu_play(series)
        elif op == "4":
            favoritos = carregar_favoritos()
            if favoritos:
                menu_play(favoritos)
            else:
                input("Nenhum favorito salvo. Enter para voltar.")
        elif op == "0":
            break
        else:
            input("Opção inválida. Enter para voltar.")

if __name__ == "__main__":
    criar_pasta()
    menu_principal()
