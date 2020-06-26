import pandas as pd
from pandas_datareader import data as web

# criando um DataFrame vazio
df = pd.DataFrame()

# escolher a ação
acao1 = 'PETR4.SA'
acao2 = 'Nasdaq'

# importar dados par o DataFrame
df = web.DataReader(acao1, data_source='yahoo', start='01-01-2000')

print(df.head())
