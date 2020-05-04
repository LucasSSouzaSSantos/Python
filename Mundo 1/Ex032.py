"""
EXERCÍCIO 032: Ano Bissexto
Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.
"""
print("-=-" * 33)
print("""Chama-se ano bissexto o ano ao qual é acrescentado um dia extra, ficando com 366 dias, 
um dia a mais do que os anos normais de 365 dias, ocorrendo a cada quatro anos 
(exceto anos múltiplos de 100 que não são múltiplos de 400). Isto é feito com o objetivo de manter 
o calendário anual ajustado com a translação da Terra e com os eventos sazonais relacionados às
estações do ano. O ano presente (2020) é bissexto. """)
print("-=-" * 33)

Ano = int(input("Informe o ano:  "))

if ((Ano % 100 != 0 and Ano % 4 == 0) or (Ano % 400 == 0)):
  print("O ano informado é BISSEXTO")
else:
  print("O ano informado não é BISSEXTO")
