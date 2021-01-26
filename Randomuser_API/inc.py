import requests
from pprint import pprint
import json

payload = {'results':4,'inc':'gender,name,nat'}
url = 'https://randomuser.me/api/'
data_list = []
try:
    responce = requests.get(url=url,params=payload)
    for i in responce.json()['results']:
        data_list.append(i)
    f = open('answer.json','w')
    data_json = json.dumps({'ExcludingFields':data_list})
    f.write(data_json)
        
except:
    print('Error')
