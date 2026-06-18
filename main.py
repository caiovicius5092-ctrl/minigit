import sys
from mygit.hashing import hashContent
from mygit.repository import criarRepositorio

#init
if len(sys.argv) > 1:
    comando = sys.argv[1]


    if comando == "init":
        nome = sys.argv[2]
        if len(sys.argv) < 3:
            nome = "projeto"
            
        criarRepositorio(nome)
        print(f"{nome} criado com sucesso")
        print(sys.argv)
    else:
        print("comando invalido")

#hash
    if comando == "hash":
        if len(sys.argv) < 3:
            print("digite o caminho do arquivo")
        else:
            print(hashContent(sys.argv[2]))
else:
    print("digite um comando")
