"""
EXERCÍCIO 050: Soma dos Pares
Desenvolva um programa que leia seis números inteiros e mostre a soma apenas
daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
"""
print(" Informe os Numeros ".center(30, '-'))
soma = 0
for x in range(0, 6, 1):
    num = float(input(f"{x + 1}° Número: ".center(30)))
    if num % 2 == 0:
        soma += num
print(f"Soma dos números pares: {soma}".center(30))
print(" ".center(30, '-'))
