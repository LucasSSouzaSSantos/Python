import json

carros_dicionario = {"marca": "honda", "modelo": "HRV", "cor": "prata"}
# dicionário -> objeto json
carros_d = json.dumps(carros_dicionario)
print("Dicionário Python para Objeto JSON: \n", carros_d)

carros_lista = ["honda", "volkswagem", "ford", "fiat", "chevrolet"]
# lista -> array json
carros_l = json.dumps(carros_lista)
print("Lista Python em Objeto JSON: \n", carros_l)

carros_tupla = ("honda", "volkswagem", "ford", "fiat", "chevrolet")
# tupla -> array json
carros_t = json.dumps(carros_tupla)
print("Tupla Python em Objeto JSON: \n", carros_t)
