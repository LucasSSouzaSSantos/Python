import os
carro = []


class Carro:
    nome = ""
    pot = 0
    velMax = 0
    ligado = False

    def __init__(self, nome, pot): # Contrutor da classe Carro
        self.nome = nome
        self.pot = pot 
        self.velMax = int(pot) * 2
        self.ligado = False 

    def ligar(self):
        self.ligado = True

    def desligar(self):
        self.ligado = False
    
    def info(self):
        print("Nome: " + self.nome)
        print("Potencia: " + str(self.pot))
        print("Velocidade Máxima: " + str(self.velMax))
        print("Ligado: " + ("Sim" if self.ligado else "Não"))


def Menu():
    os.system("clear") or None
    print("1 - Nome Carro")
    print("2 - Informações do Carro")
    print("3 - Excluir Carro")
    print("4 - Ligar Carro")
    print("5 - Desligar Carro")
    print("6 - Listar Carro")
    print("7 - Sair")
    print("Quantidade de carros " + str(len(carros)))
    opc = input("Digite um opção: ")
    return opc

def NovoCarro():
    os.system("clear") or None
    n = input("Nome do Carro: ")
    p = input("Potencia do Carro: ")
    car = Carro(n, p)
    carros.append(car)
    print("Novo carro")
    os.system("pause")


def informacoes():
    os.system("clear") or None
    n = input("Informe o número do carro que deseja ver as informações: ")
    try:
        carros[int(n)].info()
    except:
        print("Esse Carro não existe")
    os.system("pause")

def excluirCarro():
    os.system("clear") or None
    n = input("Informe o número do carro que deseja ver as informações: ")
    try:
        del carros[int(n)]
    except:
        print("Esse Carro não existe")
    os.system("pause")

def ligarCarro():
    os.system("clear") or None
    n = input("Informe o número do carro que deseja ligar: ")
    try:
        carros[int(n)].ligar()
        print("Carro Ligado")
    except:
        print("Esse Carro não existe")
    os.system("pause")


def desligarCarro():
    os.system("clear") or None
    n = input("Informe o número do carro que deseja desligar: ")
    try:
        carros[int(n)].desligar()
        print("Carro desligado")
    except:
        print("Esse Carro não existe")
    os.system("pause")


def listarCarros():
    os.system("clear") or None
    p = 0
    for c in carros:
        print(str(p) + "-" + c.nome)
        p = p + 1
    os.system("pause")
