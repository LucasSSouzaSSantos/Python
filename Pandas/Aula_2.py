# como leio e escrevo dados tabulares ?
import pandas as pd

# importando os dados

arquivo = pd.read_csv("OXY.csv")

"""
Por padr~ao o dataframe mostra as 5 primeiras e ultimas
linhas.

Quero ver as 8 primeiras linhas
"""

print("As primeiras 8 linhas")
print(arquivo.head(8))

print(30 * "=")

"Quero ver as ultimas 10 linhas"
print("As ultimas 10 linhas")
print(arquivo.tail(10))

print(30 * "=")
print("Folha tecnica")
print(arquivo.info())
