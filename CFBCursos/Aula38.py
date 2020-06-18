import json
arquivo_json = '{"nome": "Bruno","time":"aviadores","vivo": "True",' \
               '"energia": 100,"mochila": ["perdeneira", "corda", ' \
               '"linha", "arame"],"aeronaves": [{"tipo": "transporte"' \
               ', "habilidade": 80},{"tipo": "ataque","habilidade": 100},' \
               '{"tipo": "reconhecimento", "habilidade": 50}]} '

arquivo_dicionario = json.loads(arquivo_json)
print(arquivo_dicionario)