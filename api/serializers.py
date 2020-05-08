from rest_framework import serializers
from article.models import content
 

class contentSerializer(serializers.ModelSerializer):
    class Meta:
        model = content
        fields ="__all__"