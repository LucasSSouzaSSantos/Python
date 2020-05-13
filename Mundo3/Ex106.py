"""
Exercício 106:
Faça um mini-sistema que utilize o Intrective Help do Python. O usuário vai digitar o comando e o
manual vai aparecer. Quando o usuário digitar a palavra 'FIM', o programa se encerrará.
"""


def intRectiveHelp(msg):
    print(help(msg))


while True:
    m = str(input("Qual é o nome da função: ")).lower().strip()
    if m == 'fim':
        break
    intRectiveHelp(m)

