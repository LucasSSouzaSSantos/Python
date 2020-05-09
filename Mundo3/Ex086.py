"""
EXERCÍCIO 086: Matriz em Python
Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
0 [_][_][_]
1 [_][_][_]
2 [_][_][_]
   0  1  2
No final, mostre a matriz na tela, com a formatação correta.
"""
matriz = [[], [], []]
print("Informe os valores da matriz: ")
for x in range(0, 3):
    for y in range(0, 3):
        num = int(input(": "))
        matriz[x].append(num)
for x in matriz:
    for c in range(0, 3):
        print(f"{x[c]}".center(2), end=' ')
    print("")
