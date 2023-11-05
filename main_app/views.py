from django.shortcuts import render
from django.http import HttpResponse
from .models import User, Stats, Message
from .forms import CreateNewUser, MessageForm
from django.shortcuts import render, redirect
# Create your views here.

def welcome(request):
    return render(request, 'main_app/welcome.html')

#DB
def profile(response, id):
    prof = User.objects.get(id=id)
    return render(response, "main_app/profile.html", {"prof":prof})

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


def message_list(request):
    # Query the database for messages and pass them to the template
    messages = Message.objects.all()
    context = {'messages': messages}
    return render(request, 'main_app/message_list.html', context)

def add_message(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()  # Save the message to the database
            return redirect('message_list')  # Redirect to the message list page

    else:
        form = MessageForm()

    context = {'form': form}
    return render(request, 'main_app/message_form.html', context)



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
