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

def send_message(chat_id,text):
    payload = {
        'chat_id':chat_id,
        'text':text
    }

    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
    requests.get(url,params=payload)

last_update_id = -1

while True:
    chat_id,update_id,text = get_updates()
    if last_update_id != update_id:
        print(text)
        send_message(chat_id,text)
        last_update_id = update_id