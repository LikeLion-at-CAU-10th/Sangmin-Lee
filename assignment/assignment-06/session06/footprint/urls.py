from . import views
from django.urls import path

urlpatterns = [
    path("", views.footprint_GET),
    # send로 길안내하면 POST함수 찾아감.
    path("send", views.footprint_POST)
]