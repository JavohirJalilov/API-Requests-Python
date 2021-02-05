import requests
import os
from pprint import pprint

KEY = os.environ['KEY']
TOKEN = os.environ['TOKEN']

def getUpdates()->tuple:
    responce = requests.get(f'https://api.telegram.org/bot{TOKEN}/getUpdates')
    data = responce.json()['result'][-1]

    chat_id = data['message']['chat']['id']
    text = data['message']['text']
    update_id = data['update_id']

    return chat_id,text,update_id

def getWeather(text:str)->str:
    payload = {
        'q':text,
        'appid':KEY
    }
    url = 'https://api.openweathermap.org/data/2.5/weather'
    responce = requests.get(url,params=payload)
    if responce.status_code == 200:
        responce = responce.json()
        name = responce['name']
        description = responce['weather'][0]['description']
        icon = responce['weather'][0]['icon']
        temp = round(responce['main']['temp'] - 273)
        text = f"From: {name}\nDescription: {description}\nTemp: {temp}\nIcon: {icon}"
    else:
        text = 'Bunday shahar mavjud emas.\nIltimos qaytadan urinib ko\'ring'
    return text



def sendMessage(chat_id:int,text:str):
    payload = {
        'chat_id':chat_id,
        'text':text
    }
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
    requests.get(url,payload)

last_update_id = -1
while True:
    chat_id,text,update_id = getUpdates()
    if last_update_id != update_id:
        if text == '/start':
            sendMessage(chat_id,'Shahar kiriting !')
        elif text != '/start':
            text = text.title()
            sendMessage(chat_id,getWeather(text))
            
        last_update_id = update_id