"""
Ex 096: Faça um programa que tenha uma função chamada area(), que receba as dimensões de um terreno retangular
(largura e comprimento) e mostre a área do terreno.
"""


def area():
    print("Controle do Terreno")
    print(20 * '-')
    largura = float(input("Largura (m): "))
    altura = float(input("Altura (m): "))
    print(f"A área de um terreno {largura} x {altura} é {altura * largura} m².")


area()
