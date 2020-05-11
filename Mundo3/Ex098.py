"""
Exercício 098:
Faça um programa que tenha uma função chamada contador(), que receba três
parâmetros: início, fim e passo e realize a contagem.
Seu programa tem que realizar três contagens através da função criada:
a) De 1 até 10, de 1 em 1
b) De 10 atté 0, de 2 em 2
c) Uma contatem personalizada.
"""
from time import sleep


def contador():
    print("Contagem de 1 até 10 de 1 em 1.")
    for x in range(1, 11, 1):
        print(f"{x}", end=' ')
        sleep(0.3)
    print("FIM")
    print(20 * '-=-')
    print("Contagem de 10 até 0 de 2 em 2.")
    for x in range(10, -1, -2):
        print(f"{x}", end=' ')
        sleep(0.3)
    print("FIM")


def contadorPersonalizado(i, f, p):
    if p > 0:
        print(f"Contagem de {i} até {f} de {p} em {p}.")
        loop(i, f, p)
    elif p < 0:
        print(f"Contagem de {i} até {f} de {-p} em {-p}.")
        loop(i, f, -p)
    else:
        if p == 0:
            print(f"Contagem de {i} até {f} de {1} em {1}.")
            loop(i, f, 1)
    print(20 * '-=-')


def loop(i, f, p):
    if f > i:
        for x in range(i, f, p):
            print(f"{x}", end=' ')
            sleep(1)
        print("FIM...")
    else:
        if i > f:
            for x in range(i, f, -p):
                print(f"{x}", end=' ')
                sleep(1)
            print("FIM...")


print(20 * '-=-')
contador()
print(20 * '-=-')
print("Agora é sua vez de personalizar")
inicio = int(input("Inicio: "))
final = int(input("FIm: "))
passo = int(input("Passo: "))
print(20 * '-=-')
contadorPersonalizado(inicio, final, passo)
