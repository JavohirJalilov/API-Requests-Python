import requests
import os
from pprint import pprint

KEY = os.environ['KEY']
TOKEN = os.environ['TOKEN']

def getUpdates()->tuple:
    responce = requests.get(f'https://api.telegram.org/bot{TOKEN}/getUpdates')
    data = responce.json()['result'][-1]
    chat_id = data['message']['chat']['id']
    text = data['message'].get('text')
    update_id = data['update_id']

    return chat_id,text,update_id

def getLocation():
    responce = requests.get(f'https://api.telegram.org/bot{TOKEN}/getUpdates')
    data = responce.json()['result'][-1]
    location = data['message'].get('location')
    lat = location.get('latitude')
    lan = location.get('longitude')
    print(lat,lan)
    return lat,lan

def sendMessage(chat_id:int,text:str):
    button = {'text':'Location ','request_location':True}
    keyboard = [[button]]
    reply_markup = {'keyboard':keyboard,'resize_keyboard':True}
    payload = {
        'chat_id':chat_id,
        'text':text,
        'reply_markup':reply_markup
    }
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
    requests.get(url,json=payload)

chat_id,text,update_id = getUpdates()
location = getLocation()


