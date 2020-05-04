"""
EXERCÍCIO 017: Catetos e Hipotenusa
Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente
de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.
"""
cateto_oposto = float(input("Cateto oposto: "))
cateto_adjacente = float(input("Cateto adjacente: "))

print(f"A hipotenusa do triângulo é: {pow(pow(cateto_oposto, 2) + pow(cateto_adjacente, 2), 1/2)}")
