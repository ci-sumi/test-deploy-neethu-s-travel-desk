# destination/urls.py

from django.urls import path
from . import views
from .views import (
    destination_list,
    destination_create,
    destination_detail,
    mydestination,
    destination_update,
    destination_delete,
    favorite_destination,
    my_favorites,
    likes_destination,
)

urlpatterns = [
    path('', destination_list, name='destination_list'),
    path('destination/create/', destination_create, name='destination_create'),
    path('<int:id>/', destination_detail, name='destination_detail'),
    path('my-destinations/', mydestination, name='mydestination'),
    path('update/<int:destination_id>/', destination_update, name='destination_update'),
    path('delete/<int:destination_id>/', destination_delete, name='destination_delete'),
    path('favorite/<int:destination_id>/', favorite_destination, name='favorite_destination'),
    path('my-favorites/', my_favorites, name='my_favorites'),
    path('like/<int:destination_id>/', likes_destination, name='likes_destination'),
]
