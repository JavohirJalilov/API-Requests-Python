import requests

key = '66c318d009dd44edbf4cc378f81c8dbc'
headers = {'X-Api-Key':key}
url = 'https://randommer.io/api/Card'
payload = {
    'type':'Visa'
}
responce = requests.get(url,params=payload,headers=headers)

print(responce.json())