import requests

url = 'http://httpbin.org/get'
pagina = requests.get(url)
print(f"{pagina}")
