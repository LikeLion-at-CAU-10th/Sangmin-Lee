from django.urls import path
from .views import CreateView, LikeLionCreateview, LikeLionListView, ListView, DeleteView, UpdateView, DetailView

urlpatterns = [

    path('create/', LikeLionCreateview.as_view(), name='likelion_create'),
    path('list/', LikeLionListView.as_view(), name='likelion_list'),
    path('update/<int:pk>', LikeLionCreateview.as_view(), name='likelion_create'),
    # 
    path('detail/<int:pk>', LikeLionListView.as_view(), name='likelion_detail'),

    # path('create/', LikeLionCreateview.as_view(), name='likelion_create'),

]