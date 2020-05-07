from django import forms
from . import models

class createArticle(forms.ModelForm):
    class Meta:
        model = models.content
        fields = ['title','body','thumbnail']