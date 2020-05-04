"""
EXERCÍCIO 051: Progressão Aritmética
Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
No final, mostre os 10 primeiros termos dessa progressão.
"""
num = 1
print(" PROGRESSÃO ARITMÉTRICA ".center(40, '-'))
primeiro = int(input(f"a{num} = ".center(20, ' ')))
razão = int(input("r = ".center(20, ' ')))
print(" ".center(40, '-'))
print()

for x in range(primeiro, primeiro + 10 * razão, razão):
    print(f"a{num} = {x}", end=' ')
    if num % 3 == 0:
        print()
    num += 1
print("\n")
print(" ".center(40, '-'))
