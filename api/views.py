from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.models import Article
from api.models import MaskHistory
from api.serializers import ArticleSerializer
from api.serializers import MaskHistorySerializer

import requests
from bs4 import BeautifulSoup

# 해당 날짜 기사 반환
@api_view(['GET'])
def article(request):
    if request.method == 'GET':
        date = request.GET.get('date')
        article = Article.objects.filter(date=date)
        serializer = ArticleSerializer(article, many=True)
        return Response(serializer.data)

# 확진자 수 반환
@api_view(['GET'])
def confirmPerson(request):
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

@api_view(['GET', 'PUT'])
def maskHistory(request):
    if request.method == 'GET':
        date = request.GET.get('date')
        maskHistory = MaskHistory.objects.filter(date=date)
        
        serializer = MaskHistorySerializer(maskHistory, many=True)
        print(serializer)
        return Response(serializer.data[0])
    elif request.method == 'PUT':
        date = request.data['params']['date']
        withMask = request.data['params']['withMask']

        try:
            maskHistory = MaskHistory.objects.get(date=date)
            
            data={'date':date, 'outing':maskHistory.outing+1, 'wearing':maskHistory.wearing}
            if(withMask):
                data['wearing'] += 1

            serializer = MaskHistorySerializer(maskHistory, data=data)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except MaskHistory.DoesNotExist:
            data={'date':date, 'outing':1, 'wearing':0}
            if(withMask):
                data['wearing'] += 1

            serializer = MaskHistorySerializer(data=data)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        