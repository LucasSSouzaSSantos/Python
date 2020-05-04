"""
EXERCÍCIO 015: Aluguel de Carros
Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado
e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar,
sabendo que o carro custa R$ 60 por dia e R$ 0,15 por km rodado.
"""
kilometragem = float(input("Digite a quantidade de Km percorrido: "))
dias = int(input("Digite a quantidade de dias: "))

print(f"O preço do carro é: {60 * dias + 0.15 * kilometragem}")
