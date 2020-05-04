"""
EXERCÍCIO 069: Análise de Dados do Grupo
Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada,
o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
A) Quantas pessoas têm mais de 18 anos.
B) Quantos homens foram cadastrados.
C) Quantas mulheres têm menos de 20 anos.
"""
pessoasMaisDe18 = 0
homensCadastrado = 0
mulheresMenos20 = 0
cont = 0
while True:
    cont += 1
    idade = int(input("Idade: "))
    sexo = str(input("Sexo: ")).upper().strip()
    if idade > 18:
        pessoasMaisDe18 += 1
    if sexo[0] == 'M':
        homensCadastrado += 1
    if sexo[0] == 'F' and idade < 20:
        mulheresMenos20 += 1
    continuar = str(input("Continuar[Ss/Nn]: ")).upper().strip()
    while continuar not in ('S', 'N'):
        continuar = str(input("Continuar[Ss/Nn]: ")).upper().strip()
    if continuar == 'N':
        break
print(f"Pessoas cadastradas: {cont}")
print(f"Mas de 18: {pessoasMaisDe18}")
print(f"Homens cadastrado: {homensCadastrado}")
print(f"Mulheres com menos de 20 anos: {mulheresMenos20}")

