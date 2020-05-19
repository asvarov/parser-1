import csv
import datetime
import requests
import time

"""
https://www.fl.ru/projects/4395023/dlya-spiska-domenov-opredelit-datu-registratsii-domena-i-chislo-dney-registratsii-domena.html
"""

url = 'http://api.whois.vu/'
date_format = "%Y-%m-%d"


def timeit(method):
    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()
        if 'log_time' in kw:
            name = kw.get('log_name', method.__name__.upper())
            kw['log_time'][name] = int((te - ts) * 1000)
        else:
            print('%r  %2.2f ms' % (method.__name__, (te - ts) * 1000))
        return result
    return timed


@timeit
def readfile():
    with open('domains.txt') as f:
        domains = f.read().splitlines()
        domains_list = []
        for i in domains:
            domains_list.append({'q': i})
    return domains_list


@timeit
def calculate():
    params = readfile()
    domains = []
    today_date = datetime.datetime.fromtimestamp(time.time()).strftime(date_format)
    for param in params:
        request = requests.get(url, params=param)
        response = request.json()
        if request.status_code == 200:
            domain = response["domain"]
            created_epoch = response["created"]
            created = datetime.datetime.fromtimestamp(created_epoch).strftime(date_format)
            count_days = datetime.datetime.strptime(today_date, date_format) - datetime.datetime.strptime(created, date_format)
            domains.append({'domain': domain, 'registered': created, 'days_ago': count_days.days})
        else:
            print('Error!')
    return domains


@timeit
def write_csv():
    domains = calculate()
    with open("domains.csv", "w", newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        writer.writerow(['Domain name', 'Registered date', 'Days ago'])
        for item in domains:
            writer.writerow([item['domain'], item['registered'], item['days_ago']])


def main():
    write_csv()


if __name__ == "__main__":
    main()
