import argparse
import requests
from bs4 import BeautifulSoup

base_url = 'https://habr.com/ru/search'

def get_html(url):
    response = requests.get(url)
    return response.text

def parse_publications(html):
    soup = BeautifulSoup(html, 'html.parser')
    publications = soup.find_all('article', class_='tm-articles-list__item')

    for publication in publications:
        title = publication.find('a', class_='tm-title__link').text
        url = base_url + publication.find('a', class_='tm-title__link')['href']
        date = publication.find('span', class_='tm-article-datetime-published').text
        author = publication.find('a', class_='tm-user-info__username').text.strip()

        print('Заголовок:', title)
        print('Дата:', date)
        print('Автор:', author)
        print('Ссылка:', url)
        print('---')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Web scraper for Habrahabr publications')
    parser.add_argument('query', type=str, help='Search query for Habrahabr')

    args = parser.parse_args()
    query = args.query

    url = f'{base_url}/?q={query}'
    html = get_html(url)

    parse_publications(html)
