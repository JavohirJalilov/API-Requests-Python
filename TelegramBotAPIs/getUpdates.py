import requests
import os
from pprint import pprint

TOKEN = os.environ['TOKEN']

responce = requests.get(f'https://api.telegram.org/bot{TOKEN}/getUpdates')

data = responce.json()
updates = data['result']

for update in updates:
    message = update['message']
    user = message['from']
    last_name = user.get('last_name',False)
    first_name = user['first_name']
    if last_name:
        full_name = first_name + " " + last_name
    else:
        full_name = first_name
    print(full_name)