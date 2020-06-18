import os
import random
from colorama import Fore, Back, Style

jogarNovamente = "s"
jogadas = 0
quemJoga = 2
maxJogadas = 9
vit = "n"
velha = [[" ", " ", " "],
         [" ", " ", " "],
         [" ", " ", " "]]


def tela():
    global velha
    global jogadas
    os.system("clear")
    print("    0   1   2")
    print("0:  " + " | " + velha[0][0] + " | " + velha[0][1] + " | " + velha[0][2])
    print("    -----------")
    print("0:  " + " | " + velha[1][0] + " | " + velha[1][1] + " | " + velha[1][2])
    print("    -----------")
    print("0:  " + " | " + velha[2][0] + " | " + velha[2][1] + " | " + velha[2][2])
    print("Jogadas: " + Fore.GREEN + str(jogadas) + Fore.RESET)


def jogadorJoga():
    global jogadas
    global quemJoga
    global vit
    global maxJogadas
    if quemJoga == 2 and jogadas < maxJogadas:
        try:
            linha = int(input("linha: "))
            coluna = int(input("coluna: "))
            while velha[linha][coluna] != " ":
                linha = int(input("linha: "))
                coluna = int(input("coluna: "))
            velha[linha][coluna] = "X"
            quemJoga = 1
            jogadas += 1
        except:
            print("Linha ou coluna invalida")
            # vit = "n"


def cpuJoga():
    global jogadas
    global quemJoga
    global vit
    global maxJogadas
    if quemJoga == 1 and jogadas < maxJogadas:
        linha = random.randint(0, 2)
        coluna = random.randint(0, 2)
        while velha[linha][coluna] != " ":
            linha = random.randint(0, 2)
            coluna = random.randint(0, 2)
        velha[linha][coluna] = "O"
        quemJoga = 2
        jogadas += 1


def verificarVitoria():
    global  velha
    vitoria = "n"
    simbolos = ["X", "O"]
    for s in simbolos:
        vitoria = "n"
        indice_linha = 0
        indice_coluna = 0
        while indice_linha < 3:
            soma = 0
            indice_coluna = 0
            while indice_coluna < 3:
                


while True:
    tela()
    jogadorJoga()
    cpuJoga()
