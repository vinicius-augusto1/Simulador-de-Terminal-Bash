import getpass
import socket
import os

def limpaTela():
    if(os.name == "nt"):
        os.system("cls")
    else:
        os.system("clear")

def chamaMkdir():
    if len(comando) > 2:
        dirEspaco = '_'.join(comando[1:]) 
        return os.mkdir(dirEspaco)
    else:
        return os.mkdir(comando[1])

def chamaPwd():
    return print(f"{os.getcwd()}")

def chamaLs():
    for i in os.listdir():
        print(f"{i}")

def chamaTouch(comando):
    if len(comando) > 2:
        touchEspaco = '_'.join(comando[1:]) 
        f = open(f"{str(touchEspaco)}", "x")
    else:
        f = open(f"{str(comando[1])}", "x")
    
def erro():
    print("Comando invalido!")

nomeUsuario = getpass.getuser()
nomeMaquina = socket.gethostname()
comando = []

limpaTela()
while True:

    comando = input(f"{nomeUsuario} @ {nomeMaquina}:~$").split(' ')
    if comando[0] in 'exitEXIT':
        break
    elif comando[0] == 'mkdir':
        chamaMkdir()
    elif comando[0] == 'pwd':
        chamaPwd()
    elif comando[0] == 'ls':
        chamaLs()
    elif comando[0] == 'touch':
        chamaTouch(comando)
    else:
        erro()
