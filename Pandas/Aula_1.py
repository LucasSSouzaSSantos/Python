# Quero começar a usar pandas
import pandas as pd

"""
Representação da tabela de dados do Pandas
                    DataFrame
        +-------+-------+-------+-------+
        |       |       |       |       |
+-------+-------+-------+-------+-------+
|       |       |       |       |       |
+-------+-------+-------+-------+-------+
|       |       |       |       |       |
+-------+-------+-------+-------+-------+-------+
|       |       |       |       |       |   row |
+-------+-------+-------+-------+-------+-------+
|       |       |       |       |       |
+-------+-------+-------+-------+-------+
                        |Column |
                        +-------+
Eu quero armazenar dados de passageiros do Titanic. 
Para vários passageiros, eu sei os dados de 
nome (caracteres)
idade (números inteiros)
sexo (masculino / feminino)
"""

df = pd.DataFrame({
    "Name": ["Braund, Mr. William Henry",
             "Allen, Mr. William Henry",
             "male, Miss. Elizabeth"],
    "Age": [22, 35, 58],
    "Sex": ["male", "male", "female"]}
)

print(df)

"""
Para armazenar dados manualmente em uma tabela, crie
um DataFrame. Ao usar um dicionário de listas Python,
as chaves do dicionário serão usadas como cabeçalhos 
de coluna e os valores em cada lista como linhas da 
DataFrame.
                                                        
A DataFrameé uma estrutura de dados bidimensional que 
pode armazenar dados de diferentes tipos (incluindo 
caracteres, números inteiros, valores de ponto flutuan
te, dados categóricos e mais) em colunas. É semelhante
a uma planilha, uma tabela SQL ou a data.frameem R.
"""
