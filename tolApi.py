import requests
import json

def u(x):
        if type(x) == type(b''):
            return x.decode('utf8')
        else:
            return x

token = 'AgAAAAAPFVH2AAIbujRgrWafYUwrtif00ZzvoJE'
base = 'https://sandbox.toloka.yandex.ru/api/v1'
headers = {"Authorization":"OAuth " + token}

def pool_status(id):
    api_url = base+'/pools/'+str(id)
    response = requests.get(api_url, headers=headers)
    if response.status_code == 200:
       return response.json()['status']
    else:
       print('Error {0}: Content: {1}'.format(response.status_code, response.content))

print(pool_status(364576))
