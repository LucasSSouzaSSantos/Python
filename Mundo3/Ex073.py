"""
EXERCÍCIO 073: Tuplas com Times de Futebol
Crie uma tupla preenchida com os 20 primeiros colocados da Tabela
do Campeonato Brasileiro de Futebol, na ordem de colocação.
Depois mostre:
A) Os 5 primeiros.
B) Os últimos 4 colocados.
C) Times em ordem alfabética.
D) Em que posição está o time da Chapecoense.
""" 
tabela = ('Flamengo', 'Santos', 'Palmeiras', 'Grêmio', 'Athletico-PR', 'São Paulo', 'Internacional',
		'Corinthians', 'Fortaleza', 'Goiais', 'Bahia', 'Vasco', 'Atlético-MG', 'Fluminênse', 'Botafogo',
	        'Ceará', 'Cruzeiro', 'CSA', 'Chapecoense', 'Avaí')
print("Os cincos primeiros da tabela são:  ")
for x in range(0, 5):
	print(f"{x + 1}- {tabela[x]}")
print("Os quatros ultimos da tabela são: ")
for x in range(16, 20):
    print(f"{x+1}- {tabela[x]}")
print("Tabela em ordem alfabética: ")
for x in range(0, 20):
    print(f"{1+x}".ljust(2)+"-".ljust(2) +f"{sorted(tabela)[x]}".ljust(20))
for x in range(0, 20):
  if tabela[x] == 'Chapecoense':
    print(f"O time da Chapecoense estar na {x + 1}° posição")
