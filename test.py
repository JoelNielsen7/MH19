import requests

result = requests.get('http://api.openweathermap.org/data/2.5/forecast?q=Minneapolis&APPID=7affa084c276e60ac6eaa71ec2e60737').json()
print(result['list'])
