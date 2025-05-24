import webbrowser  # para abrir URL no player padrão

# ... (o resto do código permanece igual)

def abrir_no_player(url):
    try:
        webbrowser.open(url)
        console.print(f"[green]Abrindo no player padrão: {url}[/green]")
    except Exception as e:
        console.print(f"[red]Erro ao abrir no player: {e}[/red]")

def menu():
    lista_canais = []
    while True:
        console.print("\n[bold cyan]Menu IPTV Completo[/bold cyan]")
        console.print("1 - Carregar lista M3U")
        console.print("2 - Mostrar canais")
        console.print("3 - Filtrar canais")
        console.print("4 - Salvar canal favorito")
        console.print("5 - Ver favoritos")
        console.print("6 - Testar canal (abrir no player)")
        console.print("7 - Sair")
        escolha = Prompt.ask("Escolha uma opção", choices=["1","2","3","4","5","6","7"])

        if escolha == "1":
            link = Prompt.ask("Cole o link M3U")
            texto = baixar_m3u(link)
            if texto:
                lista_canais = analisar_m3u(texto)
                console.print(f"[green]Lista carregada com {len(lista_canais)} canais![/green]")
            else:
                console.print("[red]Falha ao carregar a lista.[/red]")

        elif escolha == "2":
            if lista_canais:
                mostrar_canais(lista_canais)
            else:
                console.print("[yellow]Nenhuma lista carregada ainda.[/yellow]")

        elif escolha == "3":
            if not lista_canais:
                console.print("[yellow]Nenhuma lista carregada para filtrar.[/yellow]")
                continue
            filtro_nome = Prompt.ask("Filtro por nome (deixe vazio para ignorar)", default="")
            filtro_grupo = Prompt.ask("Filtro por grupo (deixe vazio para ignorar)", default="")
            mostrar_canais(lista_canais, filtro_nome=filtro_nome, filtro_grupo=filtro_grupo)

        elif escolha == "4":
            if not lista_canais:
                console.print("[yellow]Nenhuma lista carregada para salvar favorito.[/yellow]")
                continue
            mostrar_canais(lista_canais)
            idx = Prompt.ask("Digite o ID do canal para salvar nos favoritos")
            try:
                idx = int(idx)
                if 0 <= idx < len(lista_canais):
                    salvar_favorito(lista_canais[idx])
                else:
                    console.print("[red]ID inválido.[/red]")
            except ValueError:
                console.print("[red]Entrada inválida.[/red]")

        elif escolha == "5":
            if not os.path.exists(ARQ_FAVORITOS):
                console.print("[yellow]Nenhum favorito salvo ainda.[/yellow]")
            else:
                with open(ARQ_FAVORITOS, "r", encoding="utf-8") as f:
                    favoritos = f.read()
                console.print(f"[bold green]Favoritos salvo em {ARQ_FAVORITOS}:[/bold green]")
                console.print(favoritos)

        elif escolha == "6":
            if not lista_canais:
                console.print("[yellow]Nenhuma lista carregada para testar canal.[/yellow]")
                continue
            mostrar_canais(lista_canais)
            idx = Prompt.ask("Digite o ID do canal para testar (abrir no player)")
            try:
                idx = int(idx)
                if 0 <= idx < len(lista_canais):
                    abrir_no_player(lista_canais[idx]['url'])
                else:
                    console.print("[red]ID inválido.[/red]")
            except ValueError:
                console.print("[red]Entrada inválida.[/red]")

        elif escolha == "7":
            console.print("[bold]Saindo...[/bold]")
            break
