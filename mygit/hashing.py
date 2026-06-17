import hashlib

def hashContent(arquivo):
    sha256 = hashlib.sha256()


    with open(arquivo, "rb") as f:
        for bloco in iter(lambda: f.read(4096), b""):
            sha256.update(bloco)

    return sha256.hexdigest()
        
