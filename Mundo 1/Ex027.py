"""
EXERCÍCIO 027: Primeiro e Último Nome de uma Pessoa
Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro
e o último nome separadamente.
Ex: Ana Maria de Souza
Primeiro = Ana
Último = Souza
"""

nome = str(input("Nome Completo: "))

n1 = nome.find(' ')
n2 = nome.rfind(' ')
print(f"Primeiro   =  {nome[0: n1]}")
print(f"Último     = {nome[n2:]}")
