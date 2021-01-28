import requests
import os
from pprint import pprint

TOKEN = os.environ['TOKEN']

responce = requests.get(f'https://api.telegram.org/bot{TOKEN}/getMe')

data = responce.json()
pprint(data)