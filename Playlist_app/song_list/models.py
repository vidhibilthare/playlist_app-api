from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=200)
    email=models.EmailField(max_length=200)
    phone=models.IntegerField(max_length=10)
    password=models.CharField(max_length=250)

class Song(models.Model):
    songname=models.CharField(max_length=150,null=False,blank=False)
    songimage=models.ImageField(upload_to='image')
    songaudio=models.FileField(upload_to='audio')
    singer=models.CharField(max_length=200)
    songmoviename=models.CharField(max_length=200,default=None)
    uploaded=models.DateTimeField(auto_now_add=True)
