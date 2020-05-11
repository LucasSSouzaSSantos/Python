"""
Exercício 097:
Faça um programa que tenha uma função chamada escreva(), que
receba um texto qualquer como parâmentro e mostre uma
mensagem com tamanho adaptável.
ex:
escreva("Olá, Mundo!")
Saída:
~~~~~~~~~~~~~
 Olá, Mundo!
~~~~~~~~~~~~~
msg:
    - Gustavo Guanabara
    - Curso de Python no YouTube
    - CeV
"""


def escreva(msg):
    tamanho = len(msg) + 2
    print("".center(tamanho, "~"))
    print(f" {msg} ".center(tamanho, " "))
    print("".center(tamanho, "~"))


escreva('Olá, Mundo!')
escreva('Gustavo Guanabara')
escreva('Curso de Python no YouTube')
escreva('CeV')
