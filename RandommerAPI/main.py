import requests

key = '66c318d009dd44edbf4cc378f81c8dbc'
headers = {'X-Api-Key':key}
url = 'https://randommer.io/api/Card'

responce = requests.get(url,headers=headers)

print(responce.status_code)