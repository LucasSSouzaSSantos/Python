"""
EXERCÍCIO 030: Par ou Ímpar?
Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
"""
numero = int(input("Digite um número inteiro: "))

if(numero % 2 == 0):
  print("O número digitado é PAR")
else:
  print("O número digitado é IMPAR")
