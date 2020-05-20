import json
import requests
from account import login, password, email, emailpwd

HEADERS = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}


def goodgame(login, password):
    session = requests.Session()
    data = {'login': login,
            'password': password,
            'remember': '1',
            'return': 'user',
            'backurl': '',
    }
    request = session.post("https://goodgame.ru/ajax/login/", headers=HEADERS, data=data)
    return request


def alpkr(login, password):
    session = requests.Session()

    data = {'name': login,
            'pass': password,
            'op': 'Вход',
            'form_build_id': 'form - Rmtjw_g3uOT9_2wFxoatFlFmsBECyJxU4XXMgXtT - Ak',
            'form_id': 'user_login_block',
    }
    request = session.post("http://alpkr.dp.ua/?q=users/" + login, headers=HEADERS, data=data)
    return request


def olx(login, password):
    session = requests.Session()
    data = {'login[email_phone]': email,
            'login[password]': emailpwd,
            'login[zxcvbn - password - strength]': '0.0000100001',
            'login[zxcvbn - score - strength]': '1',
    }
    request = session.post("https://www.olx.ua/account/?ref%5B0%5D%5Baction%5D=myaccount&ref%5B0%5D%5Bmethod%5D=index", headers=HEADERS, data=data)
    return request

if __name__ == '__main__':

    req1 = goodgame(login, password)
    req2 = alpkr(login, password)
    req3 = olx(login, password)
    req1json = json.loads(req1.text)
    print(req1)
    print(req2.text)
    print(req1json['response'])
    print(req3.text)

