import requests
from pprint import pprint
import json

payload = {'results':10}
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
except:
    print('Eror')

pprint(data_list)