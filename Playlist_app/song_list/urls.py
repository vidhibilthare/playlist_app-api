from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf  import settings

urlpatterns = [
    path('',views.base),
    path('add/',views.add),
    path('add_song/',views.add_song),
    path('signup/',views.signup),
    path('registration/',views.registration),
    path('login_form/',views.login_form),
    path('login/',views.login),
    # path('song/',views.song),
    path('songs/',views.songs)
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

