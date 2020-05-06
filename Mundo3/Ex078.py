"""
EXERCÍCIO 078: Maior e Menor Valores na Lista
Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre
qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
"""
lista = [int(input("Número: ")), int(input("Número: ")), int(input("Número: ")), int(input("Número: "))
         , int(input("Número: "))]

maior = menor = 0
for x in range(0, len(lista)):
    if x == 0:
        maior = menor = lista[x]
    else:
        if lista[x] > maior:
            maior = lista[x]
        if lista[x] < menor:
            menor = lista[x]
print(f"A lista digitada foi: {lista}")
print(f"Maior: {maior} Menor: {menor}")
print(f"{maior} foi digitado na posição", end=' ')
for x in range(0, len(lista)):
    if lista[x] == maior:
        print(f"{x + 1}...", end=' ')
print(f"\n{menor} foi digitado na posição", end=' ')
for x in range(0, len(lista)):
    if lista[x] == menor:
        print(f"{x + 1}...", end=' ')
