"""
EXERCÍCIO 074: Maior e Menor Valores em Tupla
Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
Depois disso, mostre a listagem de números gerados e também indique o menor e o
maior valor que estão na tupla.
"""
from random import randint
lista = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
maior = menor = 0
print("Elementos da Tupla: ")
for x in range(0, 5):
  print(f"{x+1}° =" + f"{lista[x]}".rjust(2))
  if x == 0:
    maior = menor = lista[x]
  else:
    if lista[x] > maior:
      maior = lista[x]
    if lista[x] < menor:
      menor = lista[x]

print("\n" + f"Maior = {maior}" + f"\nMenor = {menor}")
