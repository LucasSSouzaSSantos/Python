"""
Exercício 100:
Faça uma programa que tenha uma lista chamada números e duas funções sorteia() e somaPar(). A primeira função vai
sortear 5 números e vai colocá-los dentro da lista e a segunda funão vai mostrar a soma entre todos os valores PARES
sorteados pela funçaõ anterior.
"""
from random import randint


def sorteia():
    numeros = []
    for x in range(0, 5):
        numeros.append(randint(0, 99))
    print(f"A lista criada foi {numeros}.")
    somaPar(numeros)


def somaPar(lst):
    s = 0
    for x in lst:
        if x % 2 == 0:
            s += x
    print(f"A soma dos números pares é {s}")


sorteia()
