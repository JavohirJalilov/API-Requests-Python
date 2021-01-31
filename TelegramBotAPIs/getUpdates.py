import requests
import os
from pprint import pprint

TOKEN = os.environ['TOKEN']

responce = requests.get(f'https://api.telegram.org/bot{TOKEN}/getUpdates')

data = responce.json()
pprint(len(data['result']))