import requests
from pprint import pprint
import json

payload = {'results':4}
url = 'https://randomuser.me/api/'

data_list = []
try:
    responce = requests.get(url,params=payload)
    data = responce.json()['results']
    for x in data:
        d = {}
        d['Gender'] = x['gender']
        d['First_name'] = x['name']['first']
        d['Last_name'] = x['name']['last']
        d['City'] = x['location']['city']
        data_list.append(d)
    f = open('answer.json','a')
    data_json = json.dumps({"RequestingMultipleUsers":data_list})
    f.write(data_json)
except:
    print('Eror')
