from bs4 import BeautifulSoup
import requests
import json

url = "https://www.ceneo.pl/60203873#tab=reviews"

#print(response.status_code) 

all_opinions = []

while(url):
    response = requests.get(url)
    page = BeautifulSoup(response.text, 'html.parser')
    opinions = page.select('div.js_product-review')
    for opinion in opinions:
        opinion_id = opinion['data-entry-id']
        author = opinion.select_one("span.user-post__author-name").get_text().strip()
        try:
            recomendation = opinion.select_one('span.user-post__author-recomendation > em').get_text().strip()
        except:
            recomendation = None
        stars = opinion.select_one('span.user-post__score-count').get_text().strip()
        content = opinion.select_one('div.user-post__text').get_text().strip()
        useful = opinion.select_one('button.vote-yes > span').get_text().strip()
        useless = opinion.select_one('button.vote-no > span').get_text().strip()
        published = opinion.select_one('span.user-post__published > time:nth-child(1)')["datetime"]
        try:
            purchased = opinion.select_one('span.user-post__published > time:nth-child(2)')["datetime"]
        except:
            purchased = None
        pros = opinion.select("div[class$=\"positives\"] ~ div.review-feature__item")
        pros = [item.get_text().strip() for item in pros]
        cons = opinion.select("div[class$=\"negatives\"] ~ div.review-feature__item")
        cons = [item.get_text().strip() for item in cons]

        single_opinion = {
            'opinion_id': opinion_id,
            'author': author,
            'recomendation': recomendation,
            'stars': stars,
            'content': content,
            'useful': useful,
            'useless': useless,
            'published': published,
            'purchased': purchased,
            'pros': pros,
            'cons': cons
        }

        all_opinions.append(single_opinion)
    try:
        url = 'https://www.ceneo.pl'+page.select_one('a.pagination__next')['href']
    except TypeError:
        url = None
        
with open('opinions/105186036.json', 'w', encoding='UTF-8') as file:
    json.dump(all_opinions, file, indent=4, ensure_ascii=False)