from django.http import HttpResponse
from django.shortcuts import render

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.models import Article
from api.serializers import ArticleSerializer

# 해당 날짜 기사 반환
@api_view(['GET'])
def getArticle(request):
    if request.method == 'GET':
        date = request.GET.get('data')
        article = Article.objects.filter(date=date).all()
        serializer = ArticleSerializer(article, many=True)
        return Response(serializer.data)