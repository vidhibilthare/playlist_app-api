from .api import *
from django.urls import path

urlpatterns = [
    path('create/',SongViewSet.as_view()),
    path('show/',SongShowViewSet.as_view()),
    path('update/<int:pk>/',SongUpdateViewSet.as_view()),
    path('delete/<int:pk>/',SongDeleteViewSet.as_view())
]
