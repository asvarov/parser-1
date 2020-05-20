import json
import requests
from account import login, password, email, emailpwd, name, pwd

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


def alpkr(name, pwd):
    session = requests.Session()
    data = {'name': name,
            'pass': pwd,
            'op': 'Вход',
            'form_build_id': 'form-HpxAZbwtVPqnAKt9aRouPY-DNU-5OP2gYUzN3AXpuro',
            'form_id': 'user_login_block',
    }
    session.post("http://alpkr.dp.ua/?q=node&destination=node", headers=HEADERS, data=data)
    response = session.get("http://alpkr.dp.ua/?q=admin/content/node")
    return response


def olx(email, emailpwd):
    session = requests.Session()
    data = {'login[email_phone]': email,
            'login[password]': emailpwd,
            'login[zxcvbn - password - strength]': '0.0000100001',
            'login[zxcvbn - score - strength]': '1',
    }
    request = session.post("https://www.olx.ua/account/?ref%5B0%5D%5Baction%5D=myaccount&ref%5B0%5D%5Bmethod%5D=index", headers=HEADERS, data=data)
    return request


if __name__ == '__main__':


#    req1 = goodgame(login, password)
#    req2 = alpkr(login, password)
    request = alpkr(name, pwd)
#    req3 = olx(email, emailpwd)
#    req1json = json.loads(req1.text)
#    print(req1)
    print(request.text)
#    print(req1json['response'])
#    print(req3.text)

