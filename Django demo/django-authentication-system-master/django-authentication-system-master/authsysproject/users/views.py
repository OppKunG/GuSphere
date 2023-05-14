from django.contrib.postgres import search
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Venue

def search_venues(request):
    if request.method=="POST":
        searched=request.POST['searched']
        venues=Venue.objects.filter(name__contains=searched)
        return render(request, 'users/search_venues.html',{'searched':searched,'venues':venues})
    else:
         return render(request, 'users/search_venues.html')

def home(request):
    return render(request, 'users/home.html')


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Hi {username}, your account was created successfully')
            return redirect('home')
    else:
        form = UserRegisterForm()

    return render(request, 'users/register.html', {'form': form})


@login_required()
def profile(request):
    return render(request, 'users/profile.html')
