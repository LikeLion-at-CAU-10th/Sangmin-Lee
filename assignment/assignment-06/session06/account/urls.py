# views.py 가져옴. ; 함수 등등 불러오기 가능.
from . import views
from django.urls import path

urlpatterns = [
    # 데이터 읽어오는 api
    path("", views.account_GET),
    # send로 길안내하면 POST함수 찾아감. ; 데이터 삽입
    path("send", views.account_POST)
]