"""
EXERCÍCIO 006: Dobro, Triplo, Raiz Quadrada
Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
"""
import math

num = int(input("Digite um número: "))

print(f"Dobro: {2 * num} triplo: {3 * num} Raiz quadrada: {pow(num, 1/2)}")
