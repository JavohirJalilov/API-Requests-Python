import requests
import os
from pprint import pprint

TOKEN = os.environ['TOKEN']
def get_updates():
    responce = requests.get(f'https://api.telegram.org/bot{TOKEN}/getUpdates')
    data = responce.json()['result'][-1]
    chat_id = data['message']['chat']['id']

    return chat_id

def sendDice(chat_id):
    url = f'https://api.telegram.org/bot{TOKEN}/sendDice'
    payload = {
        'chat_id':chat_id,
        'emoji':'⚽'
    }
    r = requests.get(url,payload)
    pprint(r.json())
# 1046157991

sendDice(1046157991)
