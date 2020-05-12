from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from .serializers import contentSerializer
from article.models import content
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from django.contrib.auth import authenticate
from rest_framework.parsers import JSONParser,FormParser
from rest_framework.decorators import parser_classes

# Create your views here.

@api_view(['GET','POST'])
def api(request):
    articles = content.objects.all()
    serial = contentSerializer(articles,many=True)

    return Response(serial.data,status=201)


@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
@parser_classes([JSONParser,FormParser])
def apilogin(request,format=None):
    username = request.data.get('username')
    password = request.data.get('password')
    content=request.data.get("_content")
    if username is None or password is None:
        return Response({'error': 'Please provide both username and password',
            "username":username,
            "password":password,
            "reaq":request.data,
            "reaqu":request.data.get("_content"),
            "type":str(type(content))
            },
                        status=HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error': 'Invalid Credentials'},
                        status=HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key},
                    status=HTTP_200_OK)



