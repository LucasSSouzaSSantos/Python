"""
EXERCÍCIO 029: Radar Eletrônico
Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80 km/h, mostre uma
mensagem dizendo que ele foi multado. A multa vai custar R$ 7,00 por cada km acima do limite.
"""

velocidade = float(input("Informe a velocidade: "))

if(velocidade > 80):
  print(f"Você foi multado e o valor da multa é {(velocidade - 80) * 7}")
else:
  print("Siga tranquilo e uma boa viagem")

