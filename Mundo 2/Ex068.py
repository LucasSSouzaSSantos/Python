"""
EXERCÍCIO 068: Jogo do Par ou Ímpar
Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o
jogador PERDER, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
"""
from random import randint
print("""- Par
- Impar
""".upper())
while True:
    num_vitoria = 0
    voce = str(input("Par[p] ou Impar[i]: ")).upper().strip()
    while voce not in 'PI':
        voce = str(input("Par[p] ou Impar[i]: ")).upper().strip()
    num_jogador = int(input("Informe seu numero: "))
    num_computador = randint(0, 10)
    soma = num_jogador + num_computador
    if (voce == 'P' and soma % 2 == 0) or (voce == 'I' and soma % 2 == 1):
        if voce == 'P':
            num_vitoria += 1
            print(f"Jogador: Par Computador: Impar\n"
                  f"Vitoria {num_vitoria}\ncomputador = {num_computador} jogador = {num_jogador}")
        else:
            print(f"Jogador: Impar Computador: Par\n"
                  f"Vitoria {num_vitoria}\ncomputador = {num_computador} jogador = {num_jogador}")
    else:
        if voce == 'P':
            num_vitoria += 1
            print(f"Jogador: Par Computador: Impar\n"
                  f"Derrota\ncomputador = {num_computador} jogador = {num_jogador}")
            break
        else:
            print(f"Jogador: Impar Computador: Par\n"
                  f"Derrota\ncomputador = {num_computador} jogador = {num_jogador}")
            break
