"""
EXERCÍCIO 034: Aumentos Múltiplos
Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para salários superiores a R$ 1.250,00, calcule um aumento de 10%.
Para inferiores ou iguais, o aumento é de 15%.
"""
salario = float(input("Qual é o valor do salário: "))

if(salario > 1250):
  salario = salario + salario * 0.1
  print(f"O novo salário é {salario} R$")
else:
  salario = salario + salario * 0.15
  print(f"O novo salário é {salario} R$")
