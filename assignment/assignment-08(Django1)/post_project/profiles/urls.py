from django.urls import path
from .views import *

urlpatterns = [
    path('create-profile/', create_profile, name='create_profile'),
    path('get-profiles-all/', get_profiles_all, name='get_profies_all'),
    path('get-profile/<int:id>', get_profile, name='get_profile'),
    path('update-profile/<int:id>', update_profile, name='update_profie'),
    path('delete-profile/<int:id>', delete_profile, name='delete_profie'),

    # 모임생성 url
    path('create-room/<int:host_id>', create_room, name='create_room'),
    # 특정 host_id 값에 해당하는 호스트가 생성한 모임 전부가져오는 url
    path('get-rooms/<int:host_id>', get_rooms, name='get_rooms'),
    
]