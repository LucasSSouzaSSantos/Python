""" EXERCÍCIO 092: Cadastro de Trabalhador em Python
Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade)
em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de
contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
"""
from datetime import datetime
ano = datetime.now()
atual = ano.year
cadastro = {'Nome do Funcionário': str(input("Nome: ")),
            'Data de Nascimento': int(input("Data de Nascimento: ").capitalize()),
            'Carteira de Trabalho': int(input("Carteira de Trabalho: "))
            }
cadastro['Idade'] = atual - cadastro['Data de Nascimento']
if cadastro['Carteira de Trabalho'] != 0:
    cadastro['Ano de Contrataçao'] = int(input("Ano de contratação: "))
    cadastro['Salario do funcionário'] = float(input("Salário: "))
    cadastro['Tempo de Trabalho'] = atual - cadastro['Ano de Contrataçao']
    cadastro['Tempo de Aposentadoria'] = atual + 40 - cadastro['Tempo de Trabalho']
    for k, v in cadastro.items():
        print(f"-No campo {k} tem o valor {v}")
else:
    for k, v in cadastro.items():
        print(f"-No campo {k} tem o valor {v}")
