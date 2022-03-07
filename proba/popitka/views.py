from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import *
from .models import *

class HeaderView(APIView):
    def get(self, *args, **kwargs):
        name = Header.objects.all()
        serializers = HeaderSerializers(name, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)

class HeaderdisView(APIView):
    def get(self, *args, **kwargs):
        name = Headerdis.objects.all()
        serializers = HeaderdisSerializers(name, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)
