"""
EXERCÍCIO 020: Sorteando uma Ordem na Lista
O mesmo professor do exercício anterior quer sortear a ordem de apresentação de trabalhos dos alunos.
Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
"""
import random

lista = ['Lucas', 'Fernando', 'Luiz', 'Maria']
lista = random.sample(lista, 4)
print(lista)
