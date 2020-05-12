"""
Exercício 102:
Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique
o número a calcular e o outro chamado show, que será um valor lógico (opcional) indicando se será
mostrado ou não na tela o processo de cálculo do fatorial.
"""


def fatorial(n, show):
    cont = n
    fat = 1
    desenvolvimento = str(cont)
    while cont > 0:
        if cont - 1 > 0:
            desenvolvimento = desenvolvimento + 'x' + str(cont -1)
        fat *= cont
        cont -= 1
    if show:
        print(20 * "-")
        print(desenvolvimento)
    return fat


num = int(input("Fatorial: "))
print(fatorial(num, False))
