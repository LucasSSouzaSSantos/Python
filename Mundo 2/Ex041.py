"""
EXERCÍCIO 041: Classificando Atletas
A Confederação Nacional de Natação precisa de um programa que leia o ano
de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JUNIOR
- Até 25 anos: SÊNIOR
- Acima: MASTER
"""
from datetime import datetime

ano = datetime.now()
ano_atual = ano.year
nasc = int(input("Ano de nascimento: "))
idade = ano_atual - nasc

if idade <= 9:
    print(f"Idade: {idade} Categoria: Mirim")
elif 9 < idade <= 14:
    print(f"Idade: {idade} Categoria: Infatil")
elif 14 < idade <= 19:
    print(f"Idade: {idade} Categoria: Junior")
elif 19 < idade <= 25:
    print(f"Idade: {idade} Categoria: Sênior")
else:
    print(f"Idade: {idade} Categoria: Master")
