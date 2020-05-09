"""
EXERCÍCIO 084: Lista Composta e Análise de Dados
Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.
"""
nome = []
peso = []
pessoasMaisPesada = []
pessoasMaisLeve = []
cont = 0
while True:
    Nome = str(input(f"Nome Pessoa {cont + 1}: ")).capitalize().strip()
    nome.append(Nome)
    Peso = float(input(f"Peso Pessoa {cont + 1}: "))
    peso.append(Peso)
    cont += 1
    opcao = str(input("Deseja continuar: ")).upper().strip()
    if opcao[0] == 'N':
        break
for x in range(0, len(peso)):
    if peso[x] >= 100:
        pessoasMaisPesada.append(nome[x])
    if peso[x] <= 50:
        pessoasMaisLeve.append(nome[x])
print(f"Lista digitada = {nome}")
print(f"A quantidade de pessoas digitadas foi {cont}")
print(f"Listagem das Pessoa Mais Pesadas = {pessoasMaisPesada}")
print(f"Listagem das Pessoas Mais leve = {pessoasMaisLeve}")
