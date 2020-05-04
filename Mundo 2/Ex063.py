"""
EXERCÍCIO 063: Sequência de Fibonacci v1.0
Escreva um programa que leia um número n inteiro qualquer e mostre
na tela os n primeiros elementos de uma Sequência de Fibonacci.
Ex: 0 → 1 → 1 → 2 → 3 → 5 → 8
"""
a = 0
b = 1
cont = 1
n = int(input("Quantidade: "))
print("".center(20, '-'))
while cont < n + 1:
    if cont == 1:
        print(f"{a}", end='  ')
    elif cont == 2:
        print(f"{b}", end='  ')
    else:
        print(f"{a + b}", end='  ')
        temp = b
        b = a + b
        a = temp
    cont += 1
    if cont % 10 == 0:
        print("\n")
print("\n" + "".center(20, '-'))
