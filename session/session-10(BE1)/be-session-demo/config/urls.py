
# from unicodedata import name
from xml.dom.minidom import Document
from django.contrib import admin
from django.urls import path, include
from posts import views

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/',views.index, name='index'),
    path('', views.http_response, name="home"),
    path('json_respose/', views.json_respose, name="json_respose"),
    # include 로 todomates app에서 관련 url 관리 ; 주의) url에 todomates/ 빼먹지 않도록!
    path('todomates/', include('todomates.urls')),
    path('posts/', include('posts.urls')),

    path('likelion/', include('likelion.urls')),

    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)