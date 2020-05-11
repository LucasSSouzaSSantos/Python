"""
EXERCÍCIO 095: Aprimorando os Dicionários
Aprimore o EXERCÍCIO 093 para que ele funcione com vários jogadores, incluindo
um sistema de visualização de detalhes do aproveitamento de cada jogador.
"""
jogadores = []
while True:
    jogador = {'Nome do Jogador': str(input("Nome do jogador: ").capitalize()),
               'Quantidade de Partidas': int(input("Quantidade de Partidas: "))}
    gols = []
    print("Quantidade de Gols: ")
    for x in range(0, jogador['Quantidade de Partidas']):
        num = int(input(f"Partida{x + 1}: "))
        gols.append(num)
    jogador['Gols'] = gols
    jogadores.append(jogador.copy())
    opcao = str(input("Deseja continuar: "))
    if opcao in 'Nn':
        break
for x, y in enumerate(jogadores):
    print(f"  - {x + 1}° cadastrado {y}")
