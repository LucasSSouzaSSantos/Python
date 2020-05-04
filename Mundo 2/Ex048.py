"""
EXERCÍCIO 048: Soma Ímpares Múltiplos de Três
Faça um programa que calcule a soma entre todos os números ímpares que
são múltiplos de três e que se encontram no intervalo de 1 até 500.
"""
soma = 0
for x in range(0, 501, 3):
    resto = x % 2
    if resto == 1:
        soma += x
print(soma)
soma = 0
for x in range(0, 501, 1):
    resto = x % 2
    if resto == 1 and x % 3 == 0:
        soma += x
print(soma)
