import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "maskDetector.settings")
import django
django.setup()

from urllib.parse import urlparse
import requests
from bs4 import BeautifulSoup

from api.models import Article



def parseArticle():
    url = 'http://ncov.mohw.go.kr/tcmBoardList.do?brdId=3&brdGubun='
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')

    list_items = soup.select("div.board_list tbody tr")

    data = []

    for item in list_items:
        id = item.select("td")[0].text
        title = item.select("td")[1].text.splitlines()[1]
        source = item.select("td")[2].text
        date = item.select("td")[3].text[:10]

        itemObject = {
            'id': id,
            'title': title,
            'source': source,
            'date': date,
        }
        data.append(itemObject)
    return data

if __name__=='__main__':
    items = parseArticle()
    for item in items:
        Article(id = item['id'], title = item['title'], source = item['source'], date = item['date']).save()