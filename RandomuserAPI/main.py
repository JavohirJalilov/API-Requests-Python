import requests
import json
from pprint import pprint

pyload = {'results':5,'nat':['US','GB']}
url = 'https://randomuser.me/api/'

responce = requests.get(url=url,params=pyload)

pprint(responce.json())