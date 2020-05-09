"""
EXERCÍCIO 087: Mais Sobre Matriz em Python
Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.
0 [_][_][_]
1 [_][_][_]
2 [_][_][_]
   0  1  2
"""
maiorSegundaFileira = 0
somaValoresPare = 0
somaTerceiraFileira = 0
matriz = [[], [], []]
print("Informe os valores da matriz: ")
for x in range(0, 3):
    for y in range(0, 3):
        num = int(input(": "))
        matriz[x].append(num)
        if matriz[x][y] % 2 == 0:
            somaValoresPare += num
        if x == 2:
            somaTerceiraFileira += num
        if x == 1 and y == 0:
            maiorSegundaFileira = num
        else:
            if x == 1 and matriz[1][y] > maiorSegundaFileira:
                maiorSegundaFileira = matriz[1][y]
for x in matriz:
    for c in range(0, 3):
        print(f"{x[c]}".center(2), end=' ')
    print("")
print(f"A soma de todos os valores pares é: {somaValoresPare}")
print(f"A soma da terceira fileira é: {somaTerceiraFileira}")
print(f"O maior valor da segunda coluna é: {maiorSegundaFileira}")
