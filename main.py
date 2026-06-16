import sys

from mygit.repository import criarRepositorio

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

else:
    print("digite um comando")

