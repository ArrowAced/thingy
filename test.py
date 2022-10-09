import requests
import os 

r = requests.post('https://webhooks.meower.org/post/home', data={'post': os.system('ls'), 'username': 'b'})
