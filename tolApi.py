import requests
import json

token = ''
base = 'https://sandbox.toloka.yandex.ru/api/v1'
headers = {"Authorization":"OAuth " + token}

def expire(pool_id):#Дата и время по UTC, когда пул нужно закрыть
    api_url = base+'/pools/'+str(pool_id)
    response = requests.get(api_url, headers=headers)
    if response.status_code == 200:
        return response.json()['will_expire']
    else:
       print('Error '+str(response.status_code))

def pool_reward(pool_id):#Плата за набор заданий в долларах США
    api_url = base+'/pools/'+str(pool_id)
    response = requests.get(api_url, headers=headers)
    if response.status_code == 200:
        return response.json()['reward_per_assignment']
    else:
       print('Error '+str(response.status_code))

def pool_status(pool_id):#Статус пула
    api_url = base+'/pools/'+str(pool_id)
    response = requests.get(api_url, headers=headers)
    if response.status_code == 200:
       return response.json()['status']
    else:
       print('Error '+str(response.status_code))

def task_overlap(pool_id):#Перекрытие заданий пула
    api_url = base+'/tasks?pool_id='+str(pool_id)
    response = requests.get(api_url, headers=headers)
    if response.status_code == 200:
        overlaps=[]
        i=0
        for item in response.json()['items']:
            overlaps[i]=item["overlap"]
            i+=1
        return overlaps
    else:
       print('Error '+str(response.status_code))
