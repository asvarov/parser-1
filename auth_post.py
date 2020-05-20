import requests

def loginbot():
    r = requests.get('https://goodgame.ru/forum')
    print(r.text)