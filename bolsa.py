import pandas as pd
from pandas_datareader import data as web
import plotly.graph_objects as go

# criando um DataFrame vazio
df = pd.DataFrame()

# escolher a ação
acao = 'ITUB3.SA'

# importar dados par o DataFrame
df = web.DataReader(acao, data_source='yahoo', start='01-01-2000')

print(df.head())

trace1 = {
    'x': df.index,
    'open': df.Open,
    'close': df.Close,
    'high': df.High,
    'low': df.Low,
    'type': 'candlestick',
    'name': acao,
    'showlegend': False
}

data = [trace1]
layout = go.Layout()

fig = go.Figure(data=data, layout=layout)
fig.show()
