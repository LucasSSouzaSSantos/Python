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
            input("Digite enter para continuar")


def cpuJoga():
    global jogadas
    global quemJoga
    global maxJogadas
    if quemJoga == 1 and jogadas < maxJogadas:
        linha = random.randrange(0, 3)
        coluna = random.randrange(0, 3)
        while velha[linha][coluna] != " ":
            linha = random.randrange(0, 3)
            coluna = random.randrange(0, 3)
        velha[linha][coluna] = "O"
        quemJoga = 2
        jogadas += 1


def verificarVitoria():
    global velha
    vitoria = "n"
    simbolos = ["X", "O"]
    for s in simbolos:
        vitoria = "n"
        # verificar linha
        indice_linha = 0
        indice_coluna = 0
        while indice_linha < 3:
            soma = 0
            indice_coluna = 0
            while indice_coluna < 3:
                if velha[indice_linha][indice_coluna] == s:
                    soma += 1
                indice_coluna += 1
            if soma == 3:
                vitoria = s
                break
            indice_linha += 1
            if vitoria != "n":
                break
            # chegou aqui!!!!!!!!

        # verificar coluna
        indice_linha = 0
        indice_coluna = 0
        while indice_coluna < 3:
            soma = 0
            indice_linha = 0
            while indice_linha < 3:
                if velha[indice_linha][indice_coluna] == s:
                    soma += 1
                indice_linha += 1
            if soma == 3:
                vitoria = s
                break
            indice_coluna += 1
            if vitoria != "n":
                break

            # verifica diagonal 1
            soma = 0
            indice_diagonal_1 = 0
            while indice_diagonal_1 < 3:
                if velha[indice_diagonal_1][indice_diagonal_1] == s:
                    soma += 1
                indice_diagonal_1 += 1
            if soma == 3:
                vitoria = s
                break

            # verifica diagonal 2
            soma = 0
            indice_diagonal_linha = 0
            indice_diagonal_coluna = 2
            while indice_diagonal_coluna >= 0:
                if velha[indice_diagonal_linha][indice_diagonal_coluna] == s:
                    soma += 1
                indice_diagonal_coluna += 1
                indice_diagonal_coluna -= 1
            if soma == 3:
                vitoria = s
                break
    return vitoria


def redefinir():
    global velha
    global jogadas
    global quemJoga
    global maxJogadas
    global vit
    jogarNovamente = "s"
    jogadas = 0
    quemJoga = 2
    maxJogadas = 9
    vit = "n"
    velha = [[" ", " ", " "],
             [" ", " ", " "],
             [" ", " ", " "]]


while True:
    tela()
    jogadorJoga()
    cpuJoga()
    tela()
    vit = verificarVitoria()
    if vit != "n" or jogadas >= maxJogadas:
        break
