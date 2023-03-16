import requests
import csv
from bs4 import BeautifulSoup as BS


url = 'https://www.marvel.com/characters'
name_hero = '/3-d-man-chandler'
link = url + name_hero
find_this = []
give = []

r = requests.get(url)
R = requests.get(link)
html = BS(r.text, 'html.parser')
soup = BS(R.text, 'html.parser')


# it's doesn't work, because don't parse script JS
# for element in html.select('.card-body__headline'):
#     print(element.text)

name = soup.find_all(class_='masthead__headline')[0].text
datas = [
    ('name', 'link', 'universe', 'other aliases', 'education', 
        'place of origin', 'identity', 'known relatives'),
    [name, link]
]

for element in soup.select('.railBioLinks'):
    datas[1].append(element.text)

with open('dataset.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerows(
        datas
    )