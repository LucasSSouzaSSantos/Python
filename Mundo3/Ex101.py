""" Exercício 101:
Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de
nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO,
OPCIONAL ou OBRIGATÓRIO nas eleições.
"""


def voto(AnoNascimento):
    from datetime import datetime
    idade = datetime.now().year - AnoNascimento
    print(f"Com {idade} anos você tem voto: ")
    if idade < 16:
        return 'VOTO NEGADO'
    elif 16 <= idade < 18 and 65 <= idade:
        return 'OPCIONAL'
    else:
        return 'OBRIGATÓRIO'


print(voto(1992))
print(voto(2010))
