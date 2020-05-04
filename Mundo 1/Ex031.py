"""
EXERCÍCIO 031: Custo da Viagem
Desenvolva um programa que pergunte a distância de uma viagem em km. Calcule o preço da
passagem, cobrando R$ 0,50 por km para viagens de até 200 km e R$ 0,45 para
viagens mais longas.
"""
quantidade = float(input("Qual será a distância percorrida: "))
Preco = 0
# calculo do preço da passagem
if ( quantidade <= 200):
  Preco = Preco +  0.5 * quantidade
  print(f"Você deve pagar um total de {Preco} R$.")
else:
  Preco = Preco + 0.45 * quantidade
  print(f"Você deve pagar um total de {Preco} R$.")
