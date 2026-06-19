from pathlib import Path

def mostrar_status():
    raiz_projeto = Path(__file__).resolve().parent.parent

    pasta_repo = None

    # Mesma lógica de busca que você já usa para achar o repositório
    for item in raiz_projeto.iterdir():
        if item.name == ".git":
            continue

        if (
            item.is_dir()
            and (item / "objects").exists()
            and (item / "refs").exists()
            and (item / "commits").exists()
        ):
            pasta_repo = item
            break

    if pasta_repo is None:
        print("Erro: Repositório não inicializado.")
        return

    pasta_objects = pasta_repo / "objects"

    # Pega a lista de todos os arquivos dentro da pasta objects
    arquivos_adicionados = list(pasta_objects.iterdir())

    if not arquivos_adicionados:
        print("Nenhum arquivo adicionado.")
    else:
        print("Arquivos adicionados:")
        for arquivo in arquivos_adicionados:
            print(f"- {arquivo.name}")
        print("\nPronto para commit.")