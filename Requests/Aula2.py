# Passando parametros em URLs
import requests

"""
url = 'http://httpbin.org/get'
payload = {'num1': 10, 'num2': 12}
pagina = requests.get(url,params=payload)
print pagina.url')
"""
url = 'http://httpbin.org/get'
pagina = requests.get(url)
# print(f"{pagina.text}")
print(f"{pagina.encoding}")

# Resposta binário
print(f"{pagina.content}")
