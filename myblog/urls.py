from django.contrib import admin
from django.urls import path,include,re_path
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static

urlpatterns = [
    
    path('admin/', admin.site.urls),
    re_path(r'^',include('article.urls')),
    url(r'^accounts/',include('accounts.urls')),
    url(r'^api/',include('api.urls')),

]

urlpatterns = urlpatterns + static(settings.MEDIA_URL,document_root= settings.MEDIA_ROOT)