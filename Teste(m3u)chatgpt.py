import requests
from urllib.parse import urlparse, parse_qs
import os

# Funções para imprimir com cores no terminal
def print_verde_top(texto):
    verde_top = "\033[1;32m"  # negrito + verde
    reset = "\033[0m"
    print(f"{verde_top}{texto}{reset}")

def print_vermelho(texto):
    vermelho = "\033[1;31m"  # negrito + vermelho
    reset = "\033[0m"
    print(f"{vermelho}{texto}{reset}")

def print_amarelo(texto):
    amarelo = "\033[1;33m"  # negrito + amarelo
    reset = "\033[0m"
    print(f"{amarelo}{texto}{reset}")

def extrair_info(link):
    try:
        parsed = urlparse(link)
        params = parse_qs(parsed.query)
        username = params.get('username', [''])[0]
        password = params.get('password', [''])[0]
        host = f"{parsed.scheme}://{parsed.netloc}"
        port = parsed.port or ("80" if parsed.scheme == "http" else "443")
        return host, port, username, password
    except Exception as e:
        print_vermelho("Erro ao extrair dados do link: " + str(e))
        return None, None, None, None

def testar_login(host, user, passwd):
    url = f"{host}/player_api.php?username={user}&password={passwd}"
    try:
        r = requests.get(url, timeout=10)
        if r.status_code != 200:
            print_vermelho("Erro HTTP ao acessar o servidor")
            return None
        data = r.json()
        if data.get("user_info", {}).get("auth", False):
            print_verde_top("Login OK! Status do usuário: " + data['user_info']['status'])
            return data
        else:
            print_vermelho("Usuário ou senha inválidos")
    except Exception as e:
        print_vermelho("Erro na requisição: " + str(e))
    return None

def baixar_lista_m3u(host, user, passwd):
    url = f"{host}/get.php?username={user}&password={passwd}&type=m3u_plus"
    try:
        r = requests.get(url, timeout=10)
        if r.status_code == 200:
            return r.text
        else:
            print_vermelho(f"Erro ao baixar lista M3U raw: {r.status_code}")
    except Exception as e:
        print_vermelho("Erro ao baixar lista M3U raw: " + str(e))
    return None

def testar_stream(url):
    try:
        r = requests.head(url, timeout=5)
        if r.status_code == 200:
            return True
    except:
        pass
    return False

def salvar_stream_online(nome_canal, url):
    pasta = "/storage/emulated/0/Hits"
    if not os.path.exists(pasta):
        os.makedirs(pasta)
    nome_arquivo = f"{nome_canal.replace(' ', '_')}.txt"
    caminho = os.path.join(pasta, nome_arquivo)
    try:
        with open(caminho, "w") as f:
            f.write(url)
        print_verde_top(f"Stream do canal '{nome_canal}' salvo em: {caminho}")
    except Exception as e:
        print_vermelho(f"Erro ao salvar stream do canal '{nome_canal}': {e}")

def encontrar_url_canal_m3u(lista_raw, nome_canal):
    if not lista_raw:
        return None
    linhas = lista_raw.splitlines()
    for i, linha in enumerate(linhas):
        if nome_canal.lower() in linha.lower():
            if i + 1 < len(linhas):
                url = linhas[i + 1].strip()
                if url.startswith("http"):
                    return url
    return None

def mostrar_canais(data, lista_m3u_raw):
    canais = data.get("available_channels", [])
    if not canais:
        print_amarelo("Nenhum canal encontrado.")
        return
    print("\n===== Canais ao Vivo (Top 30) =====")
    for canal in canais[:30]:
        cat = canal.get("category_name", "Sem categoria")
        stream_url = encontrar_url_canal_m3u(lista_m3u_raw, canal['name'])
        status = "Offline"
        if stream_url and testar_stream(stream_url):
            status = "Online"
            salvar_stream_online(canal['name'], stream_url)
            print_verde_top(f"{canal['stream_id']} - {canal['name']} ({canal['stream_type']}) [Categoria: {cat}] - Status: {status}")
        else:
            print_vermelho(f"{canal['stream_id']} - {canal['name']} ({canal['stream_type']}) [Categoria: {cat}] - Status: {status}")

def mostrar_filmes(data):
    filmes = data.get("movie_categories", [])
    if not filmes:
        print_amarelo("Nenhuma categoria de filmes encontrada.")
        return
    print("\n===== Filmes (Categorias) =====")
    for categoria in filmes:
        print(f"Categoria: {categoria.get('category_name')} - ID: {categoria.get('category_id')}")
    movie_list = data.get("movies", [])
    if movie_list:
        print("\nFilmes (Top 10):")
        for filme in movie_list[:10]:
            cat = filme.get("category_id", "Sem categoria")
            print(f"{filme.get('movie_id')} - {filme.get('name')} (Categoria ID: {cat})")
    else:
        print_amarelo("Nenhum filme listado.")

def mostrar_series(data):
    series_cats = data.get("series_categories", [])
    if not series_cats:
        print_amarelo("Nenhuma categoria de séries encontrada.")
        return
    print("\n===== Séries (Categorias) =====")
    for categoria in series_cats:
        print(f"Categoria: {categoria.get('category_name')} - ID: {categoria.get('category_id')}")
    series_list = data.get("series", [])
    if series_list:
        print("\nSéries (Top 10):")
        for serie in series_list[:10]:
            cat = serie.get("category_id", "Sem categoria")
            print(f"{serie.get('series_id')} - {serie.get('name')} (Categoria ID: {cat})")
    else:
        print_amarelo("Nenhuma série listada.")

if __name__ == "__main__":
    print("=== Teste Avançado IPTV Xtream Codes com Cores e Salvamento ===")
    m3u_link = input("Cole aqui o link M3U: ").strip()

    host, port, user, passwd = extrair_info(m3u_link)
    if not all([host, user, passwd]):
        print_vermelho("Link inválido. Verifique e tente novamente.")
    else:
        print(f"Servidor: {host}")
        print(f"Porta: {port}")
        print(f"Usuário: {user}")
        print(f"Senha: {passwd}")

        dados = testar_login(host, user, passwd)
        if dados:
            lista_raw = baixar_lista_m3u(host, user, passwd)
            mostrar_canais(dados, lista_raw)
            mostrar_filmes(dados)
            mostrar_series(dados)
