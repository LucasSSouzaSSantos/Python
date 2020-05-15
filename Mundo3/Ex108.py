"""
Adapte o código do desafio 107, criando uma função adicional chamada
moeda() que consiga mostrar os valores como uma valor monerário formatado.
"""
from modulos.moedas import metade, dobro, aumentar, diminuir, moeda

v = float(input("Digite o preço: R$ "))
print(f"A metade de {moeda(v)} é {moeda(metade(v))}")
print(f"O dobro de {moeda(v)} é {moeda(dobro(v))}")
print(f"Aumentando 10%, temos {moeda(aumentar(v, 10))}")
print(f"Reduzindo 13%, temos {moeda(diminuir(v, 13))}")