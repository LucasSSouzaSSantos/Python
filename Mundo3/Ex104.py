"""
Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante à função input()
do Python, só que fazendo a validação para aceitar apenas um valor numérico.

ex:
n = leiaInt('Digite um n')
"""


def leiaInt(msg):
    print(msg, end='')
    num = str(input(" "))
    while not num.isnumeric():
        print("\033[0;31mErro! Digite um número inteiro valido.\033[m")
        num = str(input(" "))
    num = int(num)

    return num


# programa principal
print(30 * "-")
n = leiaInt('Digite um número:')
print(f"O número que foi digitado é {n}")
