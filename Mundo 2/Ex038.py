"""
EXERCÍCIO 038: Comparando Números
Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
- O primeiro valor é maior.
- O segundo valor é maior.
- Não existe valor maior, os dois são iguais.
"""
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

if num1 > num2:
    print(f"{num1} é maior que {num2}.")
elif num2 > num1:
    print(f"{num2} é maior que {num1}.")
else:
    print(f"{num1} é igual à {num2}")
