"""
EXERCÍCIO 058: Jogo da Adivinhação v2.0
Melhore o jogo do EXERCÍCIO 028 onde o computador vai "pensar" em um número entre 0 e 10.
Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos
palpites foram necessários para vencer.
"""
from random import randint
from time import sleep
computador = randint(0, 3)
cont = 1
print("O computador pensou em um número de 0 à 10, TENTE ACERTAR: ")
sleep(1)
jogador = int(input("Diga um número: "))

while jogador != computador:
    jogador = int(input("Diga outro número: "))
    cont += 1

if cont == 1:
    print(f"Tentativas: {cont}")
    print("Nossa você é muito rápido!!!")
elif 1 < cont < 5:
    if cont ==2 or cont == 3:
        print(f"Tentativas: {cont}")
        print("Você realmente é muito bom.")
    else:
        print(f"Tentativas: {cont}")
        print("Você é bom, mas pode melhorar!")
else:
    print(f"Tentativas: {cont}")
    print("Você pode ser melhor nas próximas vezes")
