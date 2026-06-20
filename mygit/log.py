from pathlib import Path
import json

def mostrar_log():
    raiz_projeto = Path(__file__).resolve().parent.parent
    pasta_repo = None

    # Mesma lógica de busca que você já usa nos outros arquivos
    for item in raiz_projeto.iterdir():
        if item.name == ".git":
            continue
        if item.is_dir() and (item / "commits").exists():
            pasta_repo = item
            break

    if pasta_repo is None:
        print("Erro: Repositório não inicializado.")
        return

    pasta_commits = pasta_repo / "commits"
    
    # Pega apenas as pastas numéricas (1, 2, 3...)
    ids_commits = [int(p.name) for p in pasta_commits.iterdir() if p.is_dir() and p.name.isdigit()]

    if not ids_commits:
        print("Nenhum commit encontrado no histórico.")
        return

    # Ordena do maior para o menor (mais recente primeiro)
    ids_commits.sort(reverse=True)

    print("\n=== HISTÓRICO DE COMMITS ===\n")
    
    for commit_id in ids_commits:
        arquivo_json = pasta_commits / str(commit_id) / "message.json"
        
        if arquivo_json.exists():
            with open(arquivo_json, "r", encoding="utf-8") as f:
                dados = json.load(f)
                
            print(f"Commit #{commit_id}")
            print(f"Mensagem: {dados.get('message', 'Sem mensagem')}")
            print(f"Arquivos: {dados.get('arquivos', [])}")
            print("_" * 40)