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

def getWeather(text):
    payload = {
        'q':text,
        'appid':KEY
    }
    url = 'https://api.openweathermap.org/data/2.5/weather'
    responce = requests.get(url,params=payload).json()
    name = responce['name']
    description = responce['weather'][0]['description']
    icon = responce['weather'][0]['icon']
    temp = round(responce['main']['temp'] - 273)

    text = f"From: {name}\nDescription: {description}\nTemp: {temp}\nIcon: {icon}"
    return text



def sendMessage(chat_id,text):
    payload = {
        'chat_id':chat_id,
        'text':text
    }
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
    requests.get(url,payload)

chat_id,text = getUpdates()
sendMessage(chat_id,getWeather(text))