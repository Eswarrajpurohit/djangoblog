from django.urls import path,re_path
from . import views
from django.conf.urls import url



urlpatterns = [
    #url(r'^$',views.api,name='api'),
    url(r'^$',views.api,name='api'),
    #path('detail/<str:pk>/',views.apidetail,name='apidetail'),
    path('apilogin/',views.apilogin,name='apilogin'),
    path('apisignup/',views.apisignup,name='apisignup'),
    path('apilike/',views.apilike,name='apilike'),
    path('apicreate/',views.FileView.as_view(),name='apicreate')
]