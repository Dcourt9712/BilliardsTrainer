from django.shortcuts import render
from django.http import HttpResponse
from .models import User, Stats
from .forms import CreateNewUser
# Create your views here.

def profile(response, id):
    prof = User.objects.get(id=id)
    return render(response, "main_app/profile.html", {"prof":prof})

def home(response):
    return render(response, "main_app/home.html", {})

def create(response):
    if response.method == "POST":
        form = CreateNewUser(response.POST)

        if form.is_valid():
            n = form.cleaned_data["username"]
            e = form.cleaned_data["email"]
            pwd = form.cleaned_data["password"]
            
            p = User(username=n,email=e,password=pwd)
            p.save()

    else:
        form = CreateNewUser()
    return render(response, "main_app/create.html",{"form":form})

