import requests

url = 'http://localhost:3000/predict'

r = requests.post(url, json={'city':'LosAngeles'})
print(r.json())