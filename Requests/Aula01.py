# Fazendo um requisição
import requests
import json
r = requests.get('http://httpbin.org/get', auth=('user', 'pass'))
print(r.content)
"""
import requests importação do módulo para fazer requisição
url = domínio da página que foi passado como parâmetro
pagina = instância de requests
.get(url) = método para pegar as informações da url passada
"""
