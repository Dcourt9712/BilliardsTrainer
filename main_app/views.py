from django.shortcuts import render, redirect
from django.http import HttpResponse,HttpResponseRedirect
from .models import User, Stats
from .forms import CreateNewUser, loginForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse

# Create your views here.

def welcome(request):
    return render(request, 'main_app/welcome.html')
  
#DB
def profile(response, id):
    prof = User.objects.get(id=id)
    return render(response, "main_app/profile.html", {"prof":prof})

def create(response):
    if (response.method == "POST"):
        form = CreateNewUser(response.POST)

        if form.is_valid():
            n = form.cleaned_data["username"]
            e = form.cleaned_data["email"]
            pwd = form.cleaned_data["password"]
            
            p = User(username=n,email=e,password=pwd)
            p.save()
            return redirect("/login")
    else:
        form = CreateNewUser()
    return render(response, "main_app/create.html",{"form":form})

#login
def user_login(request):
    if request.method == "POST":
        login_form = loginForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data["username"]
            password = login_form.cleaned_data["password"]
            user = authenticate(username=username,password=password)
            if user:
                if user.is_active:
                    login(request,user)
                    return redirect("/") #redirect to desired page
                else:#account is inactive
                    return HttpResponse("Account is not active.")
            else:
                print("Someone tried to login and failed.")
                print("They used username: {} and password: {}".format(username,password))
                return render(request, "main_app/login.html", {"login_form":loginForm})
    else:
        return render(request, "main_app/login.html",{"login_form":loginForm})

#logout
def user_logout(request):
        logout(request)
        return redirect("/")


#Drills
def drills(request):
    return render(request,'main_app/Drills/drills.html')

def Fundamentals(request):
    return render(request,'main_app/Drills/fundamentals.html')

def Shotmaking(request):
    return render(request,'main_app/Drills/Shotmaking.html')

def Kicking(request):
    return render(request,'main_app/Drills/kicking.html')  

def Banking(request):
    return render(request,'main_app/Drills/banking.html')
      
def Safety(request):
    return render(request,'main_app/Drills/Safety.html')

def Jumping(request):
    return render(request,'main_app/Drills/Jumping.html')
#fundamentals   
def stop(request):
    return render(request,'main_app/Drills/fundamentals/stop.html')

def follow(request):
    return render(request,'main_app/Drills/fundamentals/follow.html')

def draw(request):
    return render(request,'main_app/Drills/fundamentals/draw.html')   



#shotmaking
def mill(request):
    return render(request,'main_app/Drills/shotmaking/mill.html')

def everest(request):
    return render(request,'main_app/Drills/shotmaking/everest.html')

def ladder(request):
    return render(request,'main_app/Drills/shotmaking/ladder.html')

def corner(request):
    return render(request,'main_app/Drills/shotmaking/corner.html') 

def train (request):
    return render(request,'main_app/Drills/shotmaking/train.html')
           
def follower(request):
    return render(request,'main_app/Drills/shotmaking/follower.html')   

