#!/usr/bin/env python

import requests
# openssl x509 -x509toreq -in certificate.crt -out CSR.csr -signkey privateKey.key


payload = 'username=lucas210souza@gmail.com&password='
headers = {'X-Application': 'LucasTest', 'Content-Type': 'application/x-www-form-urlencoded'}

resp = requests.post('https://identitysso-cert.betfair.com/api/certlogin', data=payload,
                     cert=('TestApp1.crt', 'client-2048.pem'), headers=headers)

if resp.status_code == 200:
    resp_json = resp.json()
    print(resp_json['loginStatus'])
    print(resp_json['sessionToken'])

else:
    print("Request failed.")
