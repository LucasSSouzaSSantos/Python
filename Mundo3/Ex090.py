"""
EXERCÍCIO 090: Dicionário em Python
Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
No final, mostre o conteúdo da estrutura na tela.
"""
aluno = {'nome': str(input("Nome do aluno: ")), 'media': float(input("Média do aluno: "))}
if aluno['media'] >= 7:
    aluno['Situacao'] = 'Aprovado Por Média'
elif aluno['media'] < 3:
    aluno['situacao'] = 'Reprovado Por Média'
else:
    aluno['situacao'] = 'Situação Não Informada'
print(aluno)
