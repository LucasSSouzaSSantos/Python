"""
EXERCÍCIO 024: Verificando as Primeiras Letras de um Texto
Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".
"""
estado = str(input("Digite o nome de um estado: ")).strip().upper()
print("O nome SANTO estar contido no Estado selecionado[sim/true:não/false]")
print("SANTO" in estado)
