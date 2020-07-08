import betfairlightweight
from betfairlightweight import filters
import pandas as pd
import numpy as np
import datetime
import json
import requests

certs_path = r'//home//lucas//Documentos//GitHub//Python//Aposta'
my_username = ""
my_password = ""
my_app_key = ""


# trading = betfairlightweight.APIClient(username=my_username, password=my_password, app_key=my_app_key,
#                                       certs=certs_path)

payload = 'username=lucas210souza@gmail.com&password='
headers = {'X-Application': 'LucasTest', 'Content-Type': 'application/x-www-form-urlencoded'}

endpoint = "https://api.betfair.com/exchange/betting/rest/v1.0/"

resp = requests.post('https://identitysso-cert.betfair.com/api/certlogin', data=payload,
                     cert=('TestApp1.crt', 'client-2048.pem'), headers=headers)
resp_json = resp.json()

header = {'X-Application': 'oWSx9xKQ68lo4Naf', 'X-Authentication': resp_json['sessionToken'],
          'content-type': 'application/json'}

json_req = '{"filter":{ }}'

url = endpoint + "listEventTypes/"

response = requests.post(url, data=json_req, headers=header)

print(json.dumps(json.loads(response.text), indent=3))
