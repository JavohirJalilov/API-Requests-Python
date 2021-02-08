import requests
import os
from pprint import pprint

TOKEN = os.environ['TOKEN']
def get_updates():
    responce = requests.get(f'https://api.telegram.org/bot{TOKEN}/getUpdates')
    data = responce.json()['result'][-1]
    chat_id = data['message']['chat']['id']

    return chat_id

def sendPhoto(chat_id):
    url = f'https://api.telegram.org/bot{TOKEN}/sendPhoto'
    photo = open('logo.jpeg','rb')
    payload = {
        'chat_id':chat_id,
        # 'photo':'https://random.dog/a1eba572-e557-474b-a023-e48ead3c2786.jpeg',
        # 'caption':'Dog Animal'
    }
    r = requests.get(url,params=payload,files={'photo':photo})
    pprint(r.json())
# 1046157991

sendPhoto(1046157991)
