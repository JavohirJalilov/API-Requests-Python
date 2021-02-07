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


def LikeDisLike():
    like = '\U0001F44D'
    dislike = '\U0001F44E'
    return like,dislike

def writeLike(chat_id,text,first_name):
    print(text)

last_update_id = -1

while True:
    chat_id,update_id,chat_id,text,first_name = getUpdates()
    like,dislike = LikeDisLike()
    if last_update_id != update_id:
        if text == like or text == dislike:
            writeLike(chat_id,text,first_name)
        last_update_id = update_id
