import sys
from mygit.hashing import hashContent
from mygit.repository import criarRepositorio
from mygit.addFile import addFile
from mygit.commit import commit
from mygit.status import mostrar_status
from mygit.log import mostrar_log

if len(sys.argv) > 1:
    comando = sys.argv[1]
#*init
    if comando == "init":
        nome = sys.argv[2]
        if len(sys.argv) < 3:
            nome = "projeto"
            
        criarRepositorio(nome)
        print(f"{nome} criado com sucesso")
#*hash
    elif comando == "hash":
        if len(sys.argv) < 3:
            print("digite o caminho do arquivo")
        else:
            print(hashContent(sys.argv[2]))
#*add 
    elif comando == "add":
        if len(sys.argv) < 3:
            print("digite o caminho do arquivo")
        else:
            addFile(sys.argv[2])
#*commit
    elif comando == "commit":
        if len(sys.argv) < 3:
            print("Erro: digite a mensagem do commit")
        else:
            mensagem = " ".join(sys.argv[2:])
            commit(mensagem)
#*status
    elif comando == "status":
        mostrar_status()
#*log
    elif comando == "log":
        mostrar_log()
#*comando invalido
    else:
        print("comando invalido")


else:
    print("digite um comando")
