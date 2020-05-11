"""
EXERCÍCIO 093: Cadastro de Jogador de Futebol
Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador
e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso
será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
"""
jogador = {'Nome do Jogador': str(input("Nome do jogador: ").capitalize()),
           'Quantidade de Partidas': int(input("Quantidade de Partidas: "))}
gols = []
print("Quantidade de Gols: ")
for x in range(0, jogador['Quantidade de Partidas']):
    num = int(input(f"Partida{x + 1}: "))
    gols.append(num)
jogador['Gols'] = gols
print(jogador)
