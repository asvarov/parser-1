import json
import requests
from account import login, password

def loginbot(login, password):
    session = requests.Session()
    data = {'login': login,
            'password': password,
            'remember': '1',
            'return': 'user',
            'backurl': '',
    }
    request = session.post("https://goodgame.ru/ajax/login/", data=data)
    return request

if __name__ == '__main__':

    req = loginbot(login, password)
    req2json = json.loads(req.text)
    print(req)
    print(req2json)
    print(req2json['response'])

