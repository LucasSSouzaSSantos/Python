"""
EXERCÍCIO 061: Progressão Aritmética v2.0
Refaça o EXERCÍCIO 051, lendo o primeiro termo e a razão de uma PA, mostrando
os 10 primeiros termos da progressão usando a estrutura while.
"""
print(" PROGRESSÃO ARITMETRICA ".center(40, '-'))
a1 = int(input("Primeiro termo: ".center(20)))
r = int(input("Razão: ".center(20)))
print("".center(40, '-'))
cont = 1
while cont <= 10:
    if cont == 1:
        print(f"a{cont} = {a1}", end=' ')
    else:
        print(f"a{cont} = {a1 + r * cont}", end=' ')
        if cont % 5 == 0:
            print()
    cont += 1
print("\n")
print("".center(40, '-'))
