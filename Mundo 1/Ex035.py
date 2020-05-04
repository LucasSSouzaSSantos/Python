"""
EXERCÍCIO 035: Analisando Triângulo v1.0
Desenvolva um programa que leia o comprimento de três retas
e diga ao usuário se elas podem ou não formar um triângulo.
"""
print("Digite o comprimento das TRÊS retas: ")
reta1 = float(input("Reta 1: "))
reta2 = float(input("Reta 2: "))
reta3 = float(input("Reta 3: "))

if (reta1 + reta2 > reta3) and (reta1 + reta3 > reta2) and (reta2 + reta3 > reta1):
  print("As retas informadas formam um triângulo")
else:
  print("As retas informadas não formam um triângulo")
