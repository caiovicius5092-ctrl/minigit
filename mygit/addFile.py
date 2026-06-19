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

    # Define onde o arquivo deve ficar na pasta objects
    arquivo_destino = pasta_objects / arquivo_origem.name

    # SE O ARQUIVO ORIGEM EXISTIR: Copia ele normalmente
    if arquivo_origem.exists():
        shutil.copy2(arquivo_origem, arquivo_destino)
        print("Arquivo adicionado com sucesso!")
    
    # SE NÃO EXISTIR: Cria um arquivo vazio direto no destino
    else:
        print(f"Arquivo '{arquivo_origem.name}' não encontrado. Criando arquivo vazio no index...")
        arquivo_destino.touch()
        print("Arquivo criado e adicionado com sucesso!")

    print(f"Destino: {arquivo_destino}")