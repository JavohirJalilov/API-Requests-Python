import requests
import os
from pprint import pprint

TOKEN = os.environ['TOKEN']

def get_updates():
    responce = requests.get(f'https://api.telegram.org/bot{TOKEN}/getUpdates')
    result = responce.json()['result'][-1]
    chat_id = result['message']['chat']['id']
    text = result['message']['text']
    update_id = result['update_id']
    return chat_id,update_id,text

print(get_updates())