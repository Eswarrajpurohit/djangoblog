from rest_framework import serializers
from article.models import content
 

class contentSerializer(serializers.ModelSerializer):
    
    thumbnail = serializers.ImageField(use_url=True)

    class Meta:
    
        model = content
        fields =('id','title','body','thumbnail','publishedDate','author')