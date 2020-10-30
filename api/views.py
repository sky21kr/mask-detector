from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.models import MaskHistory
from api.serializers import MaskHistorySerializer

import requests
from bs4 import BeautifulSoup

# 현재 상태 입력, 반환
@api_view(['GET'])
def isWithMask(request):
    if request.method == 'GET':
        maskHistory = MaskHistory.objects.last()
        
        serializer = MaskHistorySerializer(maskHistory, many=True)
        
        return Response(serializer.data[0])

# 마스크 기록 입력, 반환
@api_view(['GET', 'PUT'])
def maskHistory(request):
    if request.method == 'GET':
        date = request.GET.get('date')
        maskHistory = MaskHistory.objects.filter(date=date)
        
        serializer = MaskHistorySerializer(maskHistory, many=True)
        
        return Response(serializer.data[0])
    elif request.method == 'PUT':
        date = request.data['params']['date']
        withMask = request.data['params']['withMask']

        try:
            maskHistory = MaskHistory.objects.get(date=date)
            
            data={'date':date, 'outing':maskHistory.outing+1, 'wearing':maskHistory.wearing, 'withMask': False}
            if(withMask):
                data['wearing'] += 1
                data['withMask'] = True

            serializer = MaskHistorySerializer(maskHistory, data=data)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except MaskHistory.DoesNotExist:
            data={'date':date, 'outing':1, 'wearing':0, 'withMask': False}
            if(withMask):
                data['wearing'] += 1
                data['withMask'] = True

            serializer = MaskHistorySerializer(data=data)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        