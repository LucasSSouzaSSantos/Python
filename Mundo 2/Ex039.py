"""
EXERCÍCIO 039: Alistamento Militar
Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade,
se ele ainda vai se alistar ao serviço militar, se é a hora de se alistar, ou se já passou
do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
"""
from datetime import datetime
ano = datetime.now()
ano_atual = ano.year
ano_nascimento = int(input("Data de nascimento: "))
idade = int(ano_atual) - ano_nascimento

if idade < 18:
    tempo_resta = 18 - idade
    print(f"Resta {tempo_resta} para seu alistamento")
elif idade == 18:
    print("Ano de alistamento")
else:
    tempo_passou = idade - 18
    print(f"Passou {tempo_passou} anos do seu alistamento. Por favor regularize sua situação.")

