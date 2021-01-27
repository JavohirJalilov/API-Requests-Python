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

def differentCurrencies(url,base):
    url += 'latest'
    payload = {
        'base':base,
        'symbols':['RUB','EUR','JPY','KRW']
    }
    responce = requests.get(url=url,params=payload)
    data = responce.json()

    return data

def historyUSD(url,dateOne,dateTwo): # dataOne,dateTwo  eg: yyyy-mm-dd
    url += 'history'
    payload = {
        'start_at':dateOne,
        'end_at':dateTwo,
        'symbols':'USD'
    }

    responce = requests.get(url=url,params=payload)
    data = responce.json()
    key = f"WithRespectToThe{data['base']}History"
    value = data['rates']
    dataAnswer = {key:value}
    return dataAnswer


data = {
    'differenceCurrency':differenceCurrency(1999,2021),
    'differentCurrencies':differentCurrencies(url,'USD'),
    'HistoryUSD':historyUSD(url,'2021-01-20','2021-01-25')
}

f = open('answer.json','w')
data_Json = json.dumps(data)
f.write(data_Json)

