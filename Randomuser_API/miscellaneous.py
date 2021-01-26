import requests
from pprint import pprint
import json

payload = {'results':4,'inc':'gender,name,nat','nat':'US'}
url = 'https://randomuser.me/api/'
responce = requests.get(url=url,params=payload)

pprint(responce.json())