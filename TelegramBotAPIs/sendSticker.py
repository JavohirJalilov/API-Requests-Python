import requests
import os
from pprint import pprint

TOKEN = os.environ['TOKEN']
def get_updates():
    responce = requests.get(f'https://api.telegram.org/bot{TOKEN}/getUpdates')
    data = responce.json()['result'][-1]
    chat_id = data['message']['chat']['id']
    sticker = data['message']['sticker']
    file_id = sticker['file_id']
    print(file_id)
    # file_id = 'CAACAgIAAxkBAAM5X_wkYMdc-eYd9W11-zioYdwP8AkAAvoDAAJHFWgJvlc7F_SdVdMeBA'
    return chat_id,file_id

def send_sticker(chat_id,file_id):
    url = f'https://api.telegram.org/bot{TOKEN}/sendSticker'
    payload = {
        'chat_id':chat_id,
        'sticker':file_id
    }
    print(chat_id)
    print((file_id))

    r = requests.get(url,payload)
    pprint(r.json())

chat_id,file_id = get_updates()
send_sticker(chat_id,file_id)
