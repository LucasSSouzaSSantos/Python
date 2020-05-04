"""
EXERCÍCIO 045: Pedra, Papel e Tesoura
Crie um programa que faça o computador jogar Jokenpô com você.
"""
from random import choice
from time import sleep
print("1- Pedra\n2- Papel\n3- Tesoura\n")
jogador = int(input("Sua vez: "))
lista = ['pedra'.upper(), 'papel'.upper(), 'tesoura'.upper()]
computador = choice(lista)
print("JO...".center(20))
sleep(1)
print("KEN...".center(20))
sleep(1)
print("PÔ...".center(20))
sleep(1)
if (jogador == 1 and computador == "PEDRA") or \
   (jogador == 2 and computador == "TESOURA") or\
   (jogador == 3 and computador == "PAPEL"):
    print("Você ganhou.")
else:
    print("Sua escolha não foi boa! ")
