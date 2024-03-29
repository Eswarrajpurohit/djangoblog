from django.shortcuts import render,redirect
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from .serializers import contentSerializer
from article.models import content,testModel

from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib.auth.forms import UserCreationForm
from rest_framework.parsers import MultiPartParser,FormParser

from rest_framework.views import APIView
from rest_framework import status


# Create your views here.

@api_view(['GET'])
def putTest(request):
    test = request.POST["test"]
    testdata = testModel()
    testdata.testField = test
    testdata.save()
    return Response({"message done":"ok"},status=201)


@api_view(['GET'])
def getTest(request):
    test = testModel.objects.all()
    m=[]
    for t in test:
        m.append({"testdata":t.testField})
    return Response({"message done":m},status=201)



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
def apilogin(request):
    get = request.body
    try:
        uname = request.data["username"]
        password = request.data["password"]
        user = authenticate(request,username = uname,password=password)
        if user is not None:
            return Response({"message":"Login sucessful","id":user.id},status=201)
    except Exception as e:
        return Response({"Error":"Incorrect username or password",},status=401)


@api_view(['POST'])
def apisignup(request):
    username = request.data["username"]
    password1 = request.data["password1"]
    password2 = request.data["password2"]
    if password1 == password2:
        if User.objects.filter(username=username).exists():
            return Response({"message":"Username already taken"})
        user = User.objects.create_user(username=username,password=password1)
        user.save()
        return Response({"message":"User created"},status=201)
    else:
        return Response({"Error":"password is in correct"},status=401)


class FileView(APIView):
  parser_classes = (MultiPartParser, FormParser)
  def post(self, request, *args, **kwargs):
    file_serializer = contentSerializer(data=request.data)
    if file_serializer.is_valid():
      file_serializer.save()
      return Response(file_serializer.data, status=status.HTTP_201_CREATED)
    else:
      return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def apilike(request):
    id=request.data["id"]
    article = content.objects.get(id=id)
    if request.data["action"]=="1":
        like =article.like
        like = like +1
        article.like = like
        article.save()
        return Response({"like":like},status=201)

    elif request.data["action"]=="0":
        like =article.like
        like = like-1
        article.like = like
        article.save()
        return Response({"like":like},status=201)
    