import pandas as pd
from pandas_datareader import data as web
import plotly.graph_objects as go

# criando um DataFrame vazio
df = pd.DataFrame()

# escolher a ação
acao1 = 'ITUB3.SA'
acao2 = 'Dow 30'

# importar dados par o DataFrame
df = web.DataReader(acao2, data_source='yahoo', start='01-01-2000')

print(df.head())
