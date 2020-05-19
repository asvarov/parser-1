import csv
import datetime
import requests
import time

"""
https://www.fl.ru/projects/4395023/dlya-spiska-domenov-opredelit-datu-registratsii-domena-i-chislo-dney-registratsii-domena.html
"""

url = 'http://api.whois.vu/'
date_format = "%Y-%m-%d"
params = {'q': 'kvvp.com.ua'}


def calculate(params):
    request = requests.get(url, params=params)
    response = request.json()
    if request.status_code == 200:
        domains = []
        domain = response["domain"]
    #    available = response["available"]
    #    country = response["type"]
    #    status = response["statuses"][0]
        created_epoch = response["created"]
    #    updated_epoch = response["updated"]
    #    expires_epoch = response["expires"]
        created = datetime.datetime.fromtimestamp(created_epoch).strftime(date_format)
    #    updated = datetime.datetime.fromtimestamp(updated_epoch).strftime(date_format)
    #    expired = datetime.datetime.fromtimestamp(expires_epoch).strftime(date_format)
        today_date = datetime.datetime.fromtimestamp(time.time()).strftime(date_format)
        count_days = datetime.datetime.strptime(today_date, date_format) - datetime.datetime.strptime(created, date_format)
    #    print('Today date:', today_date)
    #    print('Domain name:', domain)
    #    print('Domain available to registration:', available)
    #    print('Domain registered in:', country)
    #    print('Domain status:', status)
    #    print('Domain created:', created)
    #    print('Domain updated:', updated)
    #    print('Domain expired:', expired)
    #    print('Domain registered', count_days.days,  'days ago!')
        domains.append({'domain': domain, 'registered': created, 'days_ago': count_days.days})
        print(domains)
        return domains

    else:
        print('Error!')


def write_csv(domains):
    with open("domains.csv", "w", newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        writer.writerow(['Domian name', 'Registered date', 'Days ago'])
        for item in domains:
            writer.writerow([item['domain'], item['registered'], item['days_ago']])


def main():
    write_csv(calculate(params))

if __name__ == "__main__":
    main()
