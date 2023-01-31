import requests
from bs4 import BeautifulSoup
import fake_headers


url = 'https://spb.hh.ru/search/vacancy?text=python&area=1&area=2'

heders_fake = fake_headers.Headers(browser='firefox', os='win').generate()

response = requests.get(url, headers=heders_fake)
soup = BeautifulSoup(response.text, 'lxml')

quotes = soup.find_all('div', class_='serp-item')

for i in quotes:
    url_href = i.find('a', class_='serp-item__title').get('href')
    heders_fake2 = fake_headers.Headers(browser='firefox', os='win').generate()
    response2 = requests.get(url_href, headers=heders_fake2)
    soup2 = BeautifulSoup(response2.text, 'lxml')

    quotes2 = soup2.find_all('div', class_='vacancy-branded-user-content')
    if len(quotes2) == 0:
        quotes2 = soup2.find_all('div', class_='g-user-content')

    if 'Django' in str(quotes2[0]) or 'Flask' in str(quotes2[0]):
        print('Тут требуетсяс Фласк или Джанго', url_href)