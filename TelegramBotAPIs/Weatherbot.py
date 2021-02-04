import requests
import os
from pprint import pprint

KEY = os.environ['KEY']
TOKEN = os.environ['TOKEN']

def getUpdates():
    responce = requests.get(f'https://api.telegram.org/bot{TOKEN}/getUpdates')
    data = responce.json()['result'][-1]

    chat_id = data['message']['chat']['id']
    text = data['message']['text']

    return chat_id,text

print(getUpdates())
    