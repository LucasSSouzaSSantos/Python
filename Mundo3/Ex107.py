from modulos import moedas

v = float(input("Digite o preço: R$ "))
print(f"A metade de {v} é {moedas.metade(v)}")
print(f"O dobro de {v} é {moedas.dobro(v)}")
print(f"Aumentando 10%, temos {moedas.aumentar(v, 10)}")
print(f"Reduzindo 13%, temos {moedas.diminuir(v, 13)}")
