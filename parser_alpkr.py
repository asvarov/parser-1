import requests
from account import name, pwd
from bs4 import BeautifulSoup


HEADERS = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}


def alpkr(name, pwd):
    session = requests.Session()
    data = {'name': name,
            'pass': pwd,
            'op': 'Вход',
            'form_build_id': 'form-HpxAZbwtVPqnAKt9aRouPY-DNU-5OP2gYUzN3AXpuro',
            'form_id': 'user_login_block',
    }
    session.post("http://alpkr.dp.ua/?q=node&destination=node", headers=HEADERS, data=data)
    html = session.get("http://alpkr.dp.ua/?q=admin/content/node").text
    return html


def get_content(html):
    posts = BeautifulSoup(html, 'html.parser')
    items = posts.find_all('tr', {'class': ['odd', 'even']})
    list_posts = []
    for item in items:
        list_posts.append({
            'title': item.find('a').get_text(strip=True),
            'author': item.find('a').find_next('a').get_text(strip=True),
            'status': item.find('a').find_next('a').find_next('td').get_text(strip=True),
            'link': 'http://alpkr.dp.ua' + item.find('td').find_next('a').get('href'),
        })
    print(list_posts)


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



if __name__ == '__main__':
    html = alpkr(name, pwd)
    get_content(html)
