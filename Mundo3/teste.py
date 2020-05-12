import pandas as pd

arquivo = pd.read_csv("teste.csv")
lista = []
for x in arquivo.values:
    lista.append(x[1])
print(lista)
