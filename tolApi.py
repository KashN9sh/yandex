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

def pool_reward(pool_id):
    api_url = base+'/pools/'+str(pool_id)
    response = requests.get(api_url, headers=headers)
    if response.status_code == 200:
        return response.json()['reward_per_assignment']
    else:
       print('Error '+str(response.status_code))


def pool_status(pool_id):
    api_url = base+'/pools/'+str(pool_id)
    response = requests.get(api_url, headers=headers)
    if response.status_code == 200:
       return response.json()['status']
    else:
       print('Error {0}: Content: {1}'.format(response.status_code, response.content))

print(pool_reward(364576))
