"""
EXERCÍCIO 055: Maior e Menor da Sequência
Faça um programa que leia o peso de cinco pessoas.
No final, mostre qual foi o maior e o menor peso lidos.
"""
maior = menor = 0

for x in range(0, 5):
    peso = float(input(f"PESO {x + 1}: "))
    if x == 0:
        menor = maior = peso
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso

print(f"Maior = {maior}\n"
      f"Menor = {menor}")
