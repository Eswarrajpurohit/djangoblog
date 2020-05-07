from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class content(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    thumbnail = models.ImageField(upload_to='pics')
    publishedDate = models.DateField(auto_now_add=True)
    author = models.ForeignKey(User,default=None,on_delete=models.CASCADE)

    def __str__(self):
        return self.title
        