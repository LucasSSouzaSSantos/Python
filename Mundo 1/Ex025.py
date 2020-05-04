"""
EXERCÍCIO 025: Procurando uma String Dentro de Outra
Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.
"""
nome = str(input("Digite o nome de uma pessoa: ")).strip().upper()
print("Existe SILVA no nome digitado? ")
print("SILVA" in nome)
