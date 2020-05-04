"""
EXERCÍCIO 054: Grupo de Maioridade
Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre
quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
"""
from datetime import datetime

ano = datetime.now()
anoAtual = ano.year
cont = 0

for x in range(0, 7):
    nascimento = int(input("Data de nascimento: "))
    idade = anoAtual - nascimento
    if idade >= 18:
        cont += 1
print(f"Maior de Idade: {cont}\n"
      f"Menor de Idade: {7 - cont}")
