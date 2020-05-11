"""
Exercício 099:
Faça um programa que tenha uma função cahamada maior(), que receba
vários parâmetros com valores inteiros.
Seu programa tem que analizar todos os valores e dizer
qual dele é o maior.
"""
from time import sleep


def maior(* num):
    if len(num) != 0:
        m = 0
        print("Analisando os valores passados...")
        for x, y in enumerate(num):
            print(y, end=' ')
            sleep(0.5)
            if x == 0:
                m = y
            else:
                if y > m:
                    m = y
        print(f"Foram passado {len(num)} valores ao todo.")
        print(f"O maior valor informado foi {m}.")
        print(10 * "-=-")
    else:
        print("Não foi passado nenhum valor")


print(10 * "-=-")
maior(4, 6, 2, 10, 3)
maior(34, 56, 13, 3)
maior(45, 78, 90)
maior(100, 234)
maior(12)
maior()
