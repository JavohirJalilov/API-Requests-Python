import requests
import os

key = os.environ['key']

headers = {'X-Api-Key':key}
url = 'https://randommer.io/api/Card'
payload = {
    'type':'Visa'
}
responce = requests.get(url,params=payload,headers=headers)

print(responce.json())