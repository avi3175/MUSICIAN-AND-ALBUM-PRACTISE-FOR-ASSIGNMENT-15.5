from django.shortcuts import render
from musician_app.models import Musician
from album_app.models import Album
def home(request):
    musician_data = Musician.objects.all()
    album_data = Album.objects.all()
    print(musician_data)
    print(album_data)
    return render(request,'base.html',{'musician_data':musician_data,'album_data':album_data})


