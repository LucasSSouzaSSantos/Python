"""
EXERCÍCIO 028: Jogo da Adivinhação v1.0
Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5
e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
O programa deverá escrever na tela se o usuário venceu ou perdeu.
"""

from random import randint
from time import sleep

computadorEscolhe = randint(0, 5)
print("Pensando...")
sleep(1)
print("Agora tem advinhar o número que o computador pensou")
usuario = int(input("Qual númeoro ele pensou ? "))
if(usuario == computadorEscolhe):
    print("Acertou")
else:
    print("Errou")
