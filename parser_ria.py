import csv
import requests
from bs4 import BeautifulSoup


HOST = 'https://auto.ria.com'
URL = HOST + '/newauto/marka-jeep/'
HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}


def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r


def get_pages_count(html):
    soup = BeautifulSoup(html, 'html.parser')
    pagination = soup.find_all('span', class_='page-item mhide')
    if pagination:
        return int(pagination[-1].get_text())
    return 1


def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='proposition')
    cars = []
    for item in items:
        cars.append({
            'title': item.find('h3', class_='proposition_name').get_text(strip=True),
            'link': HOST + item.find('h3', class_='proposition_name').find_next('a').get('href'),
            'usd_price': item.find('div', class_='proposition_price').find_next('span', class_='green').get_text(
                strip=True).replace(' $', ''),
            'uah_price': item.find('div', class_='proposition_price').find_next('span', class_='grey size13').get_text(
                strip=True).replace(' грн', ''),
            'city': item.find('div', class_='proposition_region').find_next('strong').get_text(),
            'fuel': item.find('div', class_="proposition_information").find_next('span', class_='size13').find_next(
                'span', class_='i-block').get_text(strip=True),
            'liter': item.find('div', class_="proposition_information").find_next('span', class_='size13').find_next(
                'span', class_='i-block').find_next('span', class_='i-block').get_text(strip=True).replace(' л', ''),
            'transmission': item.find('div', class_="proposition_information").find_next('span', class_='size13').find_next(
                'span', class_='size13').get_text(strip=True),
            'drive': item.find('div', class_="proposition_information").find_next('span', class_='size13').find_next(
                'span', class_='size13').find_next('span', class_='size13').get_text(strip=True),
        })
    return cars


def write_csv(cars):
    name = get_name(URL)
    with open("%s.csv" % name, "w", newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        writer.writerow(['Марка', 'Ссылка', 'usd_price', 'uah_price', 'Город', 'fuel', 'Объём', 'transmission', 'drive'])
        for car in cars:
            writer.writerow(
                [car['title'], car['link'], car['usd_price'], car['uah_price'], car['city'], car['fuel'], car['liter'],
                 car['transmission'], car['drive']])


def get_name(url):
    uri = url.split("/")[-2]
    return uri


def parse():
    html = get_html(URL)
    if html.status_code == 200:
        last_page = get_pages_count(html.text)
        cars = []
        for page in range(1, last_page + 1):
            print(f'Парсинг страницы { page } из { last_page }...')
            html = get_html(URL, params={'page': page})
            cars.extend(get_content(html.text))
        print(f'Получено {len(cars)} автомобилей')
        write_csv(cars)
        return cars
    else:
        print('Error')


parse()