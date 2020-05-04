"""
EXERCÍCIO 019: Sorteando um Item na Lista
Um professor quer sortear um dos seus quatros alunos para apagar o quadro.
Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.
"""
import random

lista = ['Lucas', 'Fernando', 'Luiz', 'Maria']

print(random.choice(lista))
