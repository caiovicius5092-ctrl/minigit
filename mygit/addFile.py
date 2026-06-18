from pathlib import Path
import shutil

def addFile(caminho_do_arquivo_do_usuario):
    raiz_projeto = Path(__file__).resolve().parent.parent

    pasta_objects = None

    for item in raiz_projeto.iterdir():

        # Ignora o Git verdadeiro
        if item.name == ".git":
            continue

        if (
            item.is_dir()
            and (item / "objects").exists()
            and (item / "refs").exists()
            and (item / "commits").exists()
        ):
            pasta_objects = item / "objects"
            break

    if pasta_objects is None:
        print("Erro: Repositório não inicializado.")
        return

    arquivo_origem = Path(caminho_do_arquivo_do_usuario).resolve()

    if not arquivo_origem.exists():
        print("Erro: Arquivo não encontrado.")
        return

    arquivo_destino = pasta_objects / arquivo_origem.name

    shutil.copy2(arquivo_origem, arquivo_destino)

    print("Arquivo adicionado com sucesso!")
    print(f"Destino: {arquivo_destino}")