from django.contrib import admin
from django.urls import path
from .views import RoomAPIView, RoomCreateView

urlpatterns = [
    path('room', RoomAPIView.as_view()),
    path('create_room', RoomCreateView.as_view()),
]