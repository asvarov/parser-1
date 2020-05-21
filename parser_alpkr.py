import csv
import json

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
    return list_posts


def get_pages_count(html):
    soup = BeautifulSoup(html, 'html.parser')
    pagination = soup.find_all('ul', class_='pager')
    for item in pagination:
        last_page_href = item.find('li', class_='last').find_next('a').get('href')
        return int(last_page_href.split("=")[-1])


def write_csv(list_posts):
    with open("alpkr_posts.csv", "w", newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        writer.writerow(['Название', 'Автор', 'Статус', 'Ссылка'])
        for post in list_posts:
            writer.writerow([post['title'], post['author'], post['status'], post['link']])


if __name__ == '__main__':
    html = alpkr(name, pwd)
    list_posts = get_content(html)
    write_csv(list_posts)
    print(get_pages_count(html))
