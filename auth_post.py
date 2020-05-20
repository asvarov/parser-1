import json
import requests
from account import login, password, email, emailpwd

HEADERS = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}


def loginbot(login, password):
    session1 = requests.Session()
    session2 = requests.Session()
    session3 = requests.Session()

    data1 = {'login': login,
            'password': password,
            'remember': '1',
            'return': 'user',
            'backurl': '',
    }

    data2 = {'name': login,
            'pass': password,
            'op': 'Вход',
            'form_build_id': 'form - Rmtjw_g3uOT9_2wFxoatFlFmsBECyJxU4XXMgXtT - Ak',
            'form_id': 'user_login_block',
    }
    data3 = {'login[email_phone]': email,
            'login[password]': emailpwd,
            'login[zxcvbn - password - strength]': '0.0000100001',
            'login[zxcvbn - score - strength]': '1',
    }


    request1 = session1.post("https://goodgame.ru/ajax/login/", headers=HEADERS, data=data1)
    request2 = session2.post("http://alpkr.dp.ua/?q=users/" + login, headers=HEADERS, data=data2)
    request3 = session2.post("https://www.olx.ua/account/?ref%5B0%5D%5Baction%5D=myaccount&ref%5B0%5D%5Bmethod%5D=index", headers=HEADERS, data=data3)
    return request1, request2, request3

if __name__ == '__main__':

    req1, req2, req3 = loginbot(login, password)
#    req2json = json.loads(req.text)
    print(req1)
    print(req2)
    print(req3.text)
#    print(req2json)
#    print(req2json['response'])

