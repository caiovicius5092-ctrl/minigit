from pathlib import Path


def criarRepositorio(nome):
    
    raiz_projeto = Path(__file__).resolve().parent.parent
    pasta = raiz_projeto / nome
    
    subpasta_objects = pasta / "objects"
    subpasta_objects.mkdir(parents=True, exist_ok=True)

    subpasta_refs = pasta / "refs"
    subpasta_refs.mkdir(parents=True, exist_ok=True)

    subpasta_commits = pasta / "commits"
    subpasta_commits.mkdir(parents=True, exist_ok=True)

    return pasta