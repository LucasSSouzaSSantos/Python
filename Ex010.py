"""
EXERCÍCIO 010: Conversor de Moedas
Crie um programa que leia quanto dinheiro uma pessoa tem na carteira
e mostre quantos Dólares ela pode comprar.
Considere U$ 1,00 = R$ 5,24
"""
reais = float(input("Quanto reais vc tem: "))

print(f"Sua quantia em dolar é: {reais / 5.24:.2}")
