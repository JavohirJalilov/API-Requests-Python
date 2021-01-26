import requests
from pprint import pprint
import json

payload = {'results':10}
url = 'https://randomuser.me/api/'

responce = requests.get(url,params=payload)
data = responce.json()['results']
pprint(data[0])