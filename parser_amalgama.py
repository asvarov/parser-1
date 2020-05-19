import csv
import requests
from bs4 import BeautifulSoup

URL = "https://www.amalgama-lab.com/songs/i/i_am_giant/death_of_you.html"
HEADERS = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}


def get_html(URL, params=None):
    r = requests.get(URL, headers=HEADERS, params=params)
    return r


def parse():
    html = get_html(URL)
    content = get_content(html.text)
    write_csv(content)
    return content


def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    title_orig = soup.find_all('h2', class_='original')
    title_trans = soup.find_all('h2', class_='translate few')
    items = soup.find_all('div', class_='string_container')
    song = []
    song.append({'original': title_orig[0].get_text(strip=True), 'translate': title_trans[0].get_text(strip=True),})
    for item in items:
        song.append({
            'original': item.find('div', class_='original').get_text(strip=True),
            'translate': item.find('div', class_='translate').get_text(strip=True),
        })
    return song


def get_name(URL):
    return URL.split("/")[-1].split(".")[0]


def write_csv(song):
    name = get_name(URL)
    with open("%s.csv" % name, "w", newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        writer.writerow(['Оригинал', 'Перевод'])
        for item in song:
            writer.writerow([item['original'], item['translate']])


def main():
    parse()


if __name__ == "__main__":
    main()
