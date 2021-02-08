import requests
import os
from pprint import pprint

TOKEN = os.environ['TOKEN']
def getUpdates():
    responce = requests.get(f'https://api.telegram.org/bot{TOKEN}/getUpdates')
    data = responce.json()['result'][-1]
    chat_id = data['message']['chat']['id']
    text = data['message']['text']

    return chat_id,text

def sendMessage(chat_id,text):
    button1 = {
        'text':'button1'
        }
    button2 = {
        'text':'button2'
        }
    keyboard = [
        [button1,button2],
        [button1]
        ]
    reply_markup = {'keyboard':keyboard,'resize_keyboard':True}
    payload = {
        'chat_id':chat_id,
        'text': text,
        'reply_markup':reply_markup
    }
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
    responce = requests.get(url,json=payload)
    pprint(responce.json())
# 1046157991
chat_id,text = getUpdates()
sendMessage(chat_id,text)





# list1 = [
#     [1]
# ]

# print(list1)