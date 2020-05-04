"""
EXERCÍCIO 018: Seno, Cosseno e Tangente
Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e
tangente desse ângulo.
"""
from math import sin, cos, tan, radians
angulo = float(input("Digite o ângulo: "))
round(angulo)
angulo = round(radians(angulo), 4)
print(f"sen({angulo}) = {round(sin(angulo), 4)} cos({angulo}) = {round(cos(angulo), 4)} "
      f"tan({angulo}) = {round(tan(angulo), 4)}")
