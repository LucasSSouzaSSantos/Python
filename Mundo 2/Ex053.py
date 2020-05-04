"""
EXERCÍCIO 053: Detector de Palíndromo
Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
"""
nome = str(input("Digite um nome: ")).upper().strip()
nome1 = ''

for x in range(len(nome) - 1, -1, -1):
    nome1 += nome[x]

if nome1 == nome:
    print(f"O nome {nome} é um PALINDROMO")
else:
    print(f"O nome {nome} não é um PALINDROMO")
