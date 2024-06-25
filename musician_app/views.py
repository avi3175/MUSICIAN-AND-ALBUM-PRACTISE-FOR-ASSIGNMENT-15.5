from django.shortcuts import render,redirect
from .forms import MusicianForm
from .models import Musician
# Create your views here.

def musician(request):
   
    if request.method == 'POST':
        form = MusicianForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    else:
        form = MusicianForm()

    return render(request,'./musician.html',{'form':form})


def edit(request,id):
    edit_music = Musician.objects.get(pk=id)
    form = MusicianForm(instance=edit_music)
    if request.method == 'POST':
        form = MusicianForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    

    return render(request,'./musician.html',{'form':form})


def delete(request,id):
    delete_music = Musician.objects.get(pk=id)
    delete_music.delete()
    return redirect('homepage')