import json

# Tranformando um json em um dicionário python
carros_json = '{"marca":"honda","modelo":"HRV", "cor":"prata"}'

carros = json.loads(carros_json)
print("JSON -> Python: ", carros)

# Transformando um dicionário python em um json
casa = {"Produto": "agua Mineral",
        "Marca": "Santa Joana",
        "Quantidade": 500
        }
casa_json = json.dumps(casa)
print("Python -> JSON: ", casa_json)
