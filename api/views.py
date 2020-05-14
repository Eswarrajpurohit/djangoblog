from django.shortcuts import render,redirect
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from .serializers import contentSerializer
from article.models import content

from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login

from rest_framework.views import APIView 
from rest_framework.parsers import FileUploadParser
from rest_framework import status


# Create your views here.

@api_view(['GET'])
def api(request):
    articles = content.objects.all()
    serial = contentSerializer(articles,many=True)

    return Response(serial.data,status=201)


@api_view(['GET'])
def apidetail(request,pk):
    articles = content.objects.get(id=pk)
    serial = contentSerializer(articles,many=False)

    return Response(serial.data,status=201)


@api_view(['POST'])
def apitest(request):
    uname = request.data["username"]
    password = request.data["password"]
    user = authenticate(request,username = uname,password=password)
    if user is not None:
        return Response({"message":"Login sucessful"},status=201)
    return Response({"Error":"Incorrect username or password"},status=401)

