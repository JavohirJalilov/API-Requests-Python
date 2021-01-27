import requests
import json
from pprint import pprint

url = 'https://api.exchangeratesapi.io/'

def differenceCurrency(yearOne,yearTwo):
    # KRW - Korea Won
    payload = {'symbols':'KRW'}
    responce1 = requests.get(url+f'{yearOne}-12-31',params=payload)
    responce2 = requests.get(url+f'{yearTwo}-01-01',params=payload)
    data1 = responce1.json()['rates']['KRW']
    data2 = responce2.json()['rates']['KRW']
    
    return abs(data2 - data1)

