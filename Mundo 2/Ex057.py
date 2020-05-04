"""
EXERCÍCIO 057: Validação de Dados
Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
Caso esteja errado, peça a digitação novamente até ter um valor correto.
"""
sexo = str(input("Digite seu sexo: "))
while sexo not in ('s', 'S', 'n', 'N'):
    sexo = str(input("Erro: Digite seu sexo novamente!"))
