"""
Exercício 105:
Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar
um dicionário com as seguintes informações:
    - Quantidade de notas
    - A maior nota
    - A menor nota
    - A média da turma
    - A situação (opcional)
Adicione também as docstrings da função.
"""


def notas(* n, s=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param s: valor opcional, indicando se deve ou não adicionar a situação
    :param n: uma ou mais notas dos alunos (aceita várias)
    :return: dicionário com várias informações sobre a situação da turma.
    """
    nota = {}
    maior = menor = soma = 0
    nota['quantidade de notas'] = len(n)
    for x, y in enumerate(n):
        soma += y
        if x == 0:
            maior = menor = y
        else:
            if y > maior:
                maior = y
            if y < menor:
                menor = y
    nota['maior nota'] = maior
    nota['menor nota'] = menor
    nota['média'] = soma / len(n)
    if s:
        if nota['média'] >= 7:
            nota['situação'] = 'APROVADO'
        elif nota['média'] < 3:
            nota['situação'] = 'REPROVADO'
        else:
            nota['situação'] = 'SITUAÇÃO NÃO INFORMADA'

    return nota


print(notas(5, 8, 7, 9, s=True))
print(notas(2, 4, 6, 8, s=True))
print(notas(1, 2, 1, 0, s=True))
