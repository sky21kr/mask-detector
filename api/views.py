from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.models import Article
from api.serializers import ArticleSerializer

import requests
from bs4 import BeautifulSoup

# 해당 날짜 기사 반환
@api_view(['GET'])
def getArticle(request):
    if request.method == 'GET':
        date = request.GET.get('date')
        article = Article.objects.filter(date=date).all()
        serializer = ArticleSerializer(article, many=True)
        return Response(serializer.data)

# 확진자 수 반환
@api_view(['GET'])
def getConfirmPerson(request):
    if request.method == 'GET':
        url = 'http://ncov.mohw.go.kr/'
        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')

        list_items = soup.select("span.data")

        confrimedPerson = int(list_items[0].text) + int(list_items[1].text)

        data = {
            'confrimedPerson': confrimedPerson
        }

        return Response(data)