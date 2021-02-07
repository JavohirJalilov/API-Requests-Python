import requests
import os
from pprint import pprint

TOKEN = os.environ['TOKEN']
def getUpdates():
    responce = requests.get(f'https://api.telegram.org/bot{TOKEN}/getUpdates')
    data = responce.json()['result'][-1]
    first_name = data['message']['chat']['first_name']
    chat_id = data['message']['chat']['id']
    text = data['message']['text']
    update_id = data['update_id']
    return chat_id,update_id,chat_id,text,first_name


getUpdates()
