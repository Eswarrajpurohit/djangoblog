from rest_framework import serializers
from article.models import content
from django.contrib.auth.models import User

class contentSerializer(serializers.ModelSerializer):

    thumbnail = serializers.ImageField(use_url=True)

    class Meta:

        model = content
        fields ="__all__"