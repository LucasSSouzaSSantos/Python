"""
Adicione ao módulo moeda.py criado nos desafios anteriores uma função
chamada resumo(), ue mostre na tela algumas informações geradas pelas
funçoes que já temos no módulo criado até aqui.
"""
from modulos import moedas

p = float(input("Digite o preço: R$"))
moedas.resumo(p, 80, 35)
