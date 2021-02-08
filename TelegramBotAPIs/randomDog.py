import requests
import os
from pprint import pprint

TOKEN = os.environ['TOKEN']
def getUpdates():
    responce = requests.get(f'https://api.telegram.org/bot{TOKEN}/getUpdates')
    data = responce.json()['result'][-1]
    chat_id = data['message']['chat']['id']
    text = data['message']['text']
    update_id = data['update_id']

    return chat_id,text,update_id

def sendMessage(chat_id:int,text:str):
    button = {'text':'Dog 🐶'}
    keyboard = [[button]]
    reply_markup = {'keyboard':keyboard,'resize_keyboard':True}
    payload = {
        'chat_id':chat_id,
        'text':text,
        'reply_markup':reply_markup
    }
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
    requests.get(url,json=payload)

def dog():
    responce = requests.get('https://random.dog/woof.json')
    url = responce.json()['url']
    return url
    
def sendPhoto(chat_id):
    photo = dog()
    payload = {
        'chat_id':chat_id,
        'photo':photo,
        'caption':'Random Dog Animal'
    }
    url = f'https://api.telegram.org/bot{TOKEN}/sendPhoto'
    r = requests.get(url,params=payload)
    return r.json()
# 1046157991

# sendPhoto(1046157991)

last_update_id = -1
while True:
    chat_id,text,update_id = getUpdates()
    if last_update_id != update_id:
        if text == '/start':
            print(1)
            sendMessage(chat_id,'Tugmani bosing \U0001F447')
        elif text == 'Dog 🐶':
            print(2)
            sendPhoto(chat_id)
            
        last_update_id = update_id

    
