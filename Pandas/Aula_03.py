import requests

r = requests.get('https://requests.readthedocs.io/pt_BR/latest/user/quickstart.html')
print(r.text)
