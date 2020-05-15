"""
Crie um pacate chamdo utilidadesCeV que tenha dois módulos internos chamados
moeda e dado.
Transfira todas as funções utilizadas nos desafios 107, 108 e 109 para o
primeiro pacote e mantenha tudo funcionando.
"""
from modulos import moedas

p = float(input("Digite o preço: R$"))
moedas.resumo(p, 80, 35)
