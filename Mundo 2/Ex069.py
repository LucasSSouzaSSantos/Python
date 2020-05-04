"""
EXERCÍCIO 069: Análise de Dados do Grupo
Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada,
o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
A) Quantas pessoas têm mais de 18 anos.
B) Quantos homens foram cadastrados.
C) Quantas mulheres têm menos de 20 anos.
"""
mais18 = 0
homensCadastrado = 0
mulheresMenos20 = 0
while True:
    idade = int(input("Idade: "))
    sexo = str(input("Sexo: "))
    if idade > 18:
        mais18 += 1
    if sexo[0] == 'M':
        homensCadastrado += 1
    if sexo[0] == 'M' and idade < 20:
        mulheresMenos20 += 1
    continuar = str(input("Continuar[Ss/Nn]: ")).upper().strip()
    while continuar not in ('S', 'N'):
        continuar = str(input("Continuar[Ss/Nn]: ")).upper().strip()
    if continuar == 'N':
        break

print(f"Mas de 18: {mais18}")
