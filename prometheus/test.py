import requests

for i in range(1, 1000):
    r = requests.get('http://localhost:4000')
    print(r.status_code)
