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

def getLocation()->tuple:
    responce = requests.get(f'https://api.telegram.org/bot{TOKEN}/getUpdates')
    data = responce.json()['result'][-1]
    location = data['message'].get('location')
    lat = location.get('latitude')
    lan = location.get('longitude')
    return lat,lan

def getWeather(lat:float,lon:float)->str:
    payload = {
        'lat':lat,
        'lon':lon,
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

last_update_id = -1
while True:
    chat_id,text,update_id = getUpdates()
    if last_update_id != update_id:
        if text == '/start':
            text = 'Location Kiriting !'
            sendMessage(chat_id,text)
        elif text == None:
            lat,lon = getLocation()
            text = getWeather(lat,lon)
            sendMessage(chat_id,text)
        else:
            text = 'Iltimos, Location Kiriting.'
            sendMessage(chat_id,text)
            
        last_update_id = update_id