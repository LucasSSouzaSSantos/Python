"""
EXERCÍCIO 023: Separando Dígitos de um Número
Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
Ex:
Digite um número: 1834
Unidade: 4
Dezena: 3
Centena: 8
Milhar: 1
"""

"""
Solução usando string não é a ideal para resolver esse tipo de problema
numero = str(input("Digite um número qualquer: "))

print(f"Unidade: {numero[3]}")
print(f"Dezena: {numero[2]}")
print(f"Centena: {numero[1]}")
print(f"Milhar: {numero[0]}")      
"""
numero = int(input("Digite um número entre 0 e 9999: "))

unidade =   numero % 10
dezena =   numero // 10 % 10
centena = numero // 10 // 10 % 10
milhar = numero // 10 // 10 // 10

print(f"Milhar    = {milhar}")
print(f"Centenas  = {centena}")
print(f"Dezena    = {dezena}")
print(f"Unidade   = {unidade}")
