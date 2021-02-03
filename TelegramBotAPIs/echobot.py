import requests
import os
from pprint import pprint

TOKEN = os.environ['TOKEN']

def get_updates():
    responce = requests.get(f'https://api.telegram.org/bot{TOKEN}/getUpdates')
    result = responce.json()['result'][-1]
    update_id = result['update_id']
    text = result['message'].get('text')
    sticker = result['message'].get('sticker')
    if sticker != None:
        sticker = sticker['file_id']
    chat_id = result['message']['chat']['id']
    return chat_id,update_id,text,sticker

get_updates()

def send_message(chat_id,text):
    payload = {
        'chat_id':chat_id,
        'text':text
    }

    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
    requests.get(url,params=payload)

def send_sticker(chat_id,file_id):
    payload = {
        'chat_id':chat_id,
        'sticker':file_id
    }
    url = f'https://api.telegram.org/bot{TOKEN}/sendSticker'
    requests.get(url,payload)

last_update_id = -1

while True:
    chat_id,update_id,text,file_id = get_updates()
    if last_update_id != update_id:
        # print(text)
        if text != None:
            send_message(chat_id,text)
        else:
            send_sticker(chat_id,file_id)
        last_update_id = update_id