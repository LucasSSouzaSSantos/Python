import json

carros_dicionario = {"marca": "honda", "modelo": "HRV", "cor": "prata"}
# dicionário -> objeto json
carros_d = json.dumps(carros_dicionario, separators=(": ", " = "))
print("Dicionário Python para Objeto JSON: \n", carros_d)

carros_lista = ["honda", "volkswagem", "ford", "fiat", "chevrolet"]
# lista -> array json
carros_l = json.dumps(carros_lista)
print("Lista Python em Objeto JSON: \n", carros_l)

carros_tupla = ("honda", "volkswagem", "ford", "fiat", "chevrolet")
# tupla -> array json
carros_t = json.dumps(carros_tupla)
print("Tupla Python em Objeto JSON: \n", carros_t)

# pode mudar o separador no caso trocar os dois pontos por um igual
# usando o parâmetro separator

# Arquivo Json

arquivo_json = '{"nome": "Bruno","time":"aviadores","vivo": "True",' \
               '"energia": 100,"mochila": ["perdeneira", "corda", ' \
               '"linha", "arame"],"aeronaves": [{"tipo": "transporte"' \
               ', "habilidade": 80},{"tipo": "ataque","habilidade": 100},' \
               '{"tipo": "reconhecimento", "habilidade": 50}]} '

arquivo_dicionario = json.loads(arquivo_json)
print(arquivo_dicionario)

