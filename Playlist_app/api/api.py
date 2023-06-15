from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from song_list.models import *
from api.serializers import *

class SongViewSet(generics.CreateAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer


class SongShowViewSet(generics.ListAPIView):
    queryset = Song.objects.all()
    serializer_class =   SongSerializer

class SongUpdateViewSet(generics.RetrieveUpdateAPIView):
    queryset = Song.objects.all()      
    serializer_class = SongSerializer

class SongDeleteViewSet(generics.DestroyAPIView):
    queryset = Song.objects.all() 
    serializer_class = SongSerializer   