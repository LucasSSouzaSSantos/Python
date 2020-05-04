"""
EXERCÍCIO 011: Pintando Parede
Faça um programa que leia a largura e a altura de uma parede em metros,
calcule a sua área e a quantidade de tinta necessária para pintá-la,
sabendo que cada litro de tinta, pinta uma área de 2 m².
"""
largura = float(input("Largura da parede: "))
altura = float(input("Altura da parede: "))

print(f"A área da parede é {largura * altura} e a quantidade de latas é {largura * altura / 2}.")
