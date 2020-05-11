from django.urls import path,re_path
from . import views
from django.conf.urls import url


urlpatterns = [
    url(r'^$',views.api,name='api'),
    url(r'^apilogin/$',views.apilogin,name='apilogin')    
]