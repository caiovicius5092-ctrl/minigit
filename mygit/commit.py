from pathlib import Path
import shutil
import json

def commit(mensagem_texto):
    raiz_projeto = Path(__file__).resolve().parent.parent

    pasta_repo = None

    # Usa a mesma lógica de busca que você criou no addFile
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
    pasta_commits = pasta_repo / "commits"

    # 1. Lê os arquivos que foram adicionados pelo addFile
    arquivos_no_objects = list(pasta_objects.iterdir())
    if not arquivos_no_objects:
        print("Nada para comitar. Adicione arquivos primeiro com o comando 'add'.")
        return

    # 2. Descobre o número do próximo commit (1, 2, 3...)
    commits_existentes = [int(p.name) for p in pasta_commits.iterdir() if p.is_dir() and p.name.isdigit()]
    proximo_id = max(commits_existentes) + 1 if commits_existentes else 1

    # 3. Cria a pasta do novo commit (ex: projeto/commits/1/)
    pasta_novo_commit = pasta_commits / str(proximo_id)
    pasta_novo_commit.mkdir(parents=True, exist_ok=True)

    # 4. Cria o arquivo message.txt com o texto do commit
    arquivo_mensagem = pasta_novo_commit / "message.json"
    contentjson = {
        "message": mensagem_texto,
        "arquivos": [arquivo.name for arquivo in arquivos_no_objects]
    }
    with open(arquivo_mensagem, "w", encoding="utf-8") as f:
        json.dump(contentjson, f, indent=4, ensure_ascii=False)

    # 5. Copia todos os arquivos da pasta 'objects' para a pasta do commit atual
    for arquivo in arquivos_no_objects:
        shutil.copy2(arquivo, pasta_novo_commit / arquivo.name)

    print(f"Commit {proximo_id} criado com sucesso!")