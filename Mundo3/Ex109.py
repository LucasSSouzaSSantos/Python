"""
Modifique as funções que foram criadas no desafio 107 para que elas aceitem
um parâmetro a mais, informando se o valor retornado por elas vai ser ou não
formatado pela função moeda() desenvolvida no desafio 108.
"""
from modulos.moedas import metade, dobro, aumentar, diminuir, moeda

v = float(input("Digite o preço: R$ "))
print(f"A metade de {moeda(v)} é {metade(v, True)}")
print(f"O dobro de {moeda(v)} é {dobro(v)}")
print(f"Aumentando 10%, temos {aumentar(v, 10)}")
print(f"Reduzindo 13%, temos {diminuir(v, 13)}")
