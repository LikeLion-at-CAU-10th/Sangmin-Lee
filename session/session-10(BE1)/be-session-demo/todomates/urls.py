from django.urls import path
from .views import *

# todomates/
urlpatterns = [
    path('create-category', create_category, name='create-category'),
    path('get-category-all', get_category_all, name='get-category-all'),
    # int형의 id 값을 넘겨줌. ; <> 안에 담아서.
    # 예를들어 url이 ~~ get-category/1 이면 id값이 1인 것만 가져옴.
    path('get-category/<int:id>', get_category, name='get-category'),
    path('new-todo/<int:category_id>', create_todo, name='create_todo'),
    
]