from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import contentSerializer
from article.models import content

# Create your views here.
@api_view(['GET'])
def api(request):
    articles = content.objects.all()
    serial = contentSerializer(articles,many=True)

    return Response(serial.data)