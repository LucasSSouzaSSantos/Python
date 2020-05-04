"""
EXERCÍCIO 004: Dissecando uma Variável
Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo
e todas as informações possíveis sobre ele.
"""

variavel = str(input("Digite qualquer coisa: "))

print(f"É numerico: {variavel.isnumeric()}")
print(f"É uma letra {variavel.isalpha()}")
print(f"É um decimal {variavel.isdecimal()}")
