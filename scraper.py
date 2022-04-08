from bs4 import BeautifulSoup
import requests

url = "https://www.ceneo.pl/105186036#tab=reviews"
response = requests.get(url)

#print(response.status_code) 

page = BeautifulSoup(response.text, 'html.parser')

opinions = page.select('div.js_product-review')
opinion = opinions.pop(0)
opinion_id = opinion['data-entry-id']
author = opinion.select_one("span.user-post__author-name").get_text().strip()
recomendation = opinion.select_one('span.user-post__author-recomendation > em').get_text().strip()
stars = opinion.select_one('span.user-post__score-count').get_text().strip()
content = opinion.select_one('div.user-post__text').get_text().strip()
useful = opinion.select_one('button.vote-yes > span').get_text().strip()
useless = opinion.select_one('button.vote-no > span').get_text().strip()
published = opinion.select_one('span.user-post__published > time:nth-child(1)')["datetime"]
purchased = opinion.select_one('span.user-post__published > time:nth-child(2)')["datetime"]

print(author)
print(recomendation)
print(stars)
print(content)
print(useful)
print(useless)
print(published)
print(published)