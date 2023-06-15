from django.shortcuts import render,redirect , HttpResponseRedirect
from django.contrib.auth.hashers import make_password,check_password
from django.contrib import messages
from .models import *
from django.http.response import HttpResponse
# Create your views here.
def base(request):
    return render(request,'base.html')



def signup(request):
    return render(request,'signup.html')

def registration(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        password = make_password(request.POST['password'])
        if User.objects.filter(email=email).exists():
            messages.error(request,'email already exists')
            return redirect('/signup/')
        elif User.objects.filter(phone=phone).exists():
            messages.error(request,'phone is already exists')
            return redirect('/signup/')
        else:
            User.objects.create(name=name,email=email,password=password,phone=phone)
            return redirect('/login/')
        
def login(request):
    return render(request,'login.html')

def login_form(request):
    if request.method == 'POST':
        email=request.POST['email']
        user_password=request.POST['password']
        if User.objects.filter(email=email).exists():
            obj=User.objects.get(email=email)
            password=obj.password
            if check_password(user_password,password):
                return redirect('/song/')
            else:
                return HttpResponse('password incorrect!!!!')
        else:
            return HttpResponse('email is not registred')

# def song(request):
#     return render(request,'song.html')

def songs(request):
    song=Song.objects.all()
    return render(request,'song.html',{'song':song})

def add(request):
    return render(request,'add.html')

def add_song(request):
    if request.method == 'POST':
        songname=request.POST['songname']
        songimage=request.FILES.get('songimage')
        songaudio=request.FILES.get('songaudio')
        singer=request.POST['singer']
        songmoviename=request.POST['songmoviename']
        Song.objects.create(songname=songname,songimage=songimage,songaudio=songaudio,singer=singer,songmoviename=songmoviename,)
        song=Song.objects.all()
        return HttpResponseRedirect('/song/')
    else:
        return render(request,'song.html')