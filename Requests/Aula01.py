# Fazendo um requisição
import requests

url = 'https://requests.readthedocs.io/pt_BR/latest/user/quickstart.html' 
requisicao_get = requests.get(url)
print(f"Requisição GET: {requisicao_get}")

"""
import requests importação do módulo para fazer requisição
url = domínio da página que foi passado como parâmetro
pagina = instância de requests
.get(url) = método para pegar as informações da url passada
"""

requisicao_post = requests.post(url)
print(f"Requisição POST: {requisicao_post}")

requisicao_put = requests.put(url)
print(f"Requisição PUT: {requisicao_put}")


requisicao_delete = requests.delete(url)
print(f"Requisição DELETE: {requisicao_delete}")
