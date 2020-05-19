import datetime
import requests
import time

"""
https://www.fl.ru/projects/4395023/dlya-spiska-domenov-opredelit-datu-registratsii-domena-i-chislo-dney-registratsii-domena.html
"""

url = 'http://api.whois.vu/'
date_format = "%Y-%m-%d"
params = {'q': 'kvvp.com.ua'}
request = requests.get(url, params=params)
response = request.json()

if request.status_code == 200:
    domain = response["domain"]
    available = response["available"]
    country = response["type"]
    status = response["statuses"][0]
    created_epoch = response["created"]
    updated_epoch = response["updated"]
    expires_epoch = response["expires"]
    created = datetime.datetime.fromtimestamp(created_epoch).strftime(date_format)
    updated = datetime.datetime.fromtimestamp(updated_epoch).strftime(date_format)
    expired = datetime.datetime.fromtimestamp(expires_epoch).strftime(date_format)
    today_date = datetime.datetime.fromtimestamp(time.time()).strftime(date_format)
    count_days = datetime.datetime.strptime(today_date, date_format) - datetime.datetime.strptime(created, date_format)
#    print('Today date:', today_date)
    print('Domain name:', domain)
#    print('Domain available to registration:', available)
#    print('Domain registered in:', country)
#    print('Domain status:', status)
    print('Domain created:', created)
#    print('Domain updated:', updated)
#    print('Domain expired:', expired)
    print('Domain registered', count_days.days,  'days ago!')
else:
    print('Error!')
