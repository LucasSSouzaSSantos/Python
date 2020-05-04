"""
EXERCÍCIO 013: Reajuste Salarial
Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
"""
salario = float(input("Informe o Salário: "))

print(f"O reajuste de {salario * 0.15} e seu novo salário é: {round(1.15 * salario, 4)}")

