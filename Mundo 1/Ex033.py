"""
EXERCÍCIO 033: Maior e Menor Valores
Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
"""
print("Informe TRÊS valores")
num1 = int(input("Primeiro: "))
num2 = int(input("Segundo: "))
num3 = int(input("Terceiro: "))

maior = menor = num1

if (num2 > num1 and num2 > num3):
  maior = num2
else:
  if(num3 > num1 and num3 > num2):
    maior = num3
if(num2 < num1 and num2 < num3):
  menor = num2
else:
  if(num3 < num1 and num3 < num2):
    menor = num3
print(f"O maior valor é {maior} e o menor é {menor}")
