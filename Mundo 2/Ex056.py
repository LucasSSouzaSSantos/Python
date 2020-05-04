"""
EXERCÍCIO 056: Analisador Completo
Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
- A média de idade do grupo.
- Qual é o nome do homem mais velho.
- Quantas mulheres têm menos de 20 anos.
"""
from datetime import datetime
ano = datetime.now()
anoAtual = ano.year

numeroMulherMaior20 = 0
somaIdade = 0
maisVelho = 0
nomeMaisVelho = ''

for x in range(0, 4):
    nome = str(input(f"Nome {x + 1} = ")).upper().strip()
    nasc = int(input("Data de Nascimento: "))
    sexo = str(input("Sexo: ")).upper().strip()
    idade = anoAtual - nasc
    somaIdade += idade
    if x == 0:
        nomeMaisVelho = nome
        maisVelho = idade
    else:
        if sexo[0] == 'F' and idade < 20:
            numeroMulherMaior20 += 1
        if sexo[0] == 'M' and idade > maisVelho:
            maisVelho = idade
            nomeMaisVelho = nome

print(f"A média de idade do grupo é {somaIdade / 4}")
print(f"A quantidade de mulhers abaixo dos 20 anos é {numeroMulherMaior20}.")
print(f"{nomeMaisVelho} é o homem mais velho com {maisVelho} anos.")
