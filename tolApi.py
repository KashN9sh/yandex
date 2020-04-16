import requests
import json

token = 'AgAAAAAPFVH2AAIbujRgrWafYUwrtif00ZzvoJE'
base = 'https://sandbox.toloka.yandex.ru/api/v1'
headers = {"Authorization":"OAuth " + token}

def pool_status(pool_id):
    api_url = base+'/pools/'+str(pool_id)
    response = requests.get(api_url, headers=headers)
    if response.status_code == 200:
       return response.json()['status']
    else:
       print('Error '+str(response.status_code))

def task_overlap(pool_id):
    api_url = base+'/tasks?pool_id='+str(pool_id)
    response = requests.get(api_url, headers=headers)
    if response.status_code == 200:
       return response.json()
    else:
       print('Error '+str(response.status_code))

print(task_overlap(364576))
