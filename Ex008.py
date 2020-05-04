"""
EXERCÍCIO 008: Conversor de Medidas
Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
"""

medida = float(input("Digite uma medida em metro: "))
print(f"{medida} m = {medida / 1000} Km")
print(f"{medida} m = {medida * 100} cm")
print(f"{medida} m = {medida * 1000} mm")
print(f"{medida} m = {medida * 10} dm")
