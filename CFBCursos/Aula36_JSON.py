import json

carros_json = '{"marca":"honda","modelo":"HRV" "cor":"prata"}'

carros = json.loads(carros_json)  # Ele vai carregar e transformar todo esse json em uma string

print(carros)
