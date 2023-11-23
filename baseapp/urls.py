from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path("categoriy/<int:cat_id>/", by_category, name='category'),
    path("create-room/", create_room, name='create-room'),
    path("update-room/<str:pk>", update_room, name='update-room'),
    path("delete-room/<str:pk>", delete_room, name='delete-room'),
    path("create-topic/", create_topic, name='create-topic'),
]
