from django.conf.urls import url
from django.urls import path,re_path
from . import views

urlpatterns = [
    re_path(r'^$', views.home,name='home'),
    url(r'^create/$',views.creat_article,name='create'),    
    path('content/<int:aid>', views.articleContent,name="content"),
    path('likes/<int:aid>/<int:action>', views.like,name="likes"),

]
