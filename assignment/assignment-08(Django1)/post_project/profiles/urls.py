from django.urls import path
from .views import *

urlpatterns = [
    path('create-profile/', create_profile, name='create_profile'),
    path('get-profiles-all/', get_profiles_all, name='get_profies_all'),
    path('get-profile/<int:id>', get_profile, name='get_profile'),
    path('update-profile/<int:id>', update_profile, name='update_profie'),
    path('delete-profile/<int:id>', delete_profile, name='delete_profie'),
    
]