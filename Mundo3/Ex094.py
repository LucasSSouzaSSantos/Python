"""
EXERCÍCIO 094: Unindo Dicionários e Listas
Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de
cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:
A) Quantas pessoas cadastradas.
B) A média de idade.
C) Uma lista com mulheres.
D) Uma lista com idade acima da média.
"""
pessoa = {}
cadastro = []
Mulheres = []
soma = 0
while True:
    pessoa['Nome de Pessoa'] = str(input("Nome: ").title().strip())
    pessoa['Sexo da Pessoa'] = str(input("Sexo: ").upper().strip())
    if pessoa['Sexo da Pessoa'][0] == 'F':
        Mulheres.append(pessoa['Nome de Pessoa'])
    pessoa['Idade da Pessoa'] = int(input("Idade: "))
    soma += pessoa['Idade da Pessoa']
    cadastro.append(pessoa.copy())
    opcao = str(input("Deseja continuar: "))
    if opcao in 'Nn':
        break
print("Cadastro: ")
print(f"  - Soma {soma}")
print(f"  - Média {round(soma / len(cadastro), 4)}")
print(" > Mulheres Cadastradas: ")
IdadeAcimaDaMedia = []
for p, n in enumerate(Mulheres):
    print(f"  - {p + 1}º cadastrada: {n}")
for p, l in enumerate(cadastro):
    if l['Idade da Pessoa'] > soma / len(cadastro):
        IdadeAcimaDaMedia.append(l['Nome de Pessoa'])
print(f" > Pessoas com idade acima da Média ")
for p, x in enumerate(IdadeAcimaDaMedia):
    print(f"  - {p + 1}º cadastrada {x}")
