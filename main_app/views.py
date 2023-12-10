from django.shortcuts import render, redirect
from django.http import HttpResponse,HttpResponseRedirect
from .forms import CreateNewUser, loginForm, MessageForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse
from .models import User, Stats, Message
from .models import Drill_data
from django.shortcuts import get_object_or_404

# Create your views here.
def welcome(request):
    return render(request, 'main_app/welcome.html')

#DB
@login_required(login_url='/login/')
def profile(response, id):
    prof = User.objects.get(id=id)
    return render(response, "main_app/profile.html", {"prof":prof})

def create(request):
    if (request.method == "POST"):
        form = CreateNewUser(request.POST)

        if form.is_valid():
            New_User = form.save()
            New_User.set_password(New_User.password)
            New_User.save()

            return redirect("/login")
    else:
        form = CreateNewUser()
    return render(request, "main_app/create.html",{"form":form})

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

@login_required(login_url='/login/')
def user_stats(request):
    context = Drill_data.objects.filter(username=request.user)
    return render(request,'main_app/user_stat.html', {'context':context} )

@login_required(login_url='/login/')
def message_list(request):
    # Query the database for messages and pass them to the template
    messages = Message.objects.all()
    context = {'messages': messages}
    return render(request, 'main_app/message_list.html', context)

@login_required(login_url='/login/')
def add_message(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save(user=request.user)  # Pass the current user to the form's save method
            return redirect('message_list')  # Redirect to the message list page

    else:
        form = MessageForm()

    context = {'form': form}
    return render(request, 'main_app/message_form.html', context)


@login_required(login_url='/login/')
def delete_message(request, message_id):
    message = get_object_or_404(Message, pk=message_id)
    if message.is_author(request.user):
        message.delete()
    return redirect('message_list')



#Drills
@login_required(login_url='/login/')
def drills(request):
    return render(request,'main_app/Drills/drills.html')

@login_required(login_url='/login/')
def Fundamentals(request):
    return render(request,'main_app/Drills/fundamentals.html')
@login_required(login_url='/login/')
def Shotmaking(request):
    return render(request,'main_app/Drills/Shotmaking.html')
@login_required(login_url='/login/')
def Kicking(request):
    return render(request,'main_app/Drills/kicking.html')

@login_required(login_url='/login/')
def Banking(request):
    return render(request,'main_app/Drills/banking.html')

@login_required(login_url='/login/')
def Safety(request):
    return render(request,'main_app/Drills/safety.html')

@login_required(login_url='/login/')
def Jumping(request):
    return render(request,'main_app/Drills/jumping.html')
#fundamentals

@login_required(login_url='/login/')
def stop(request):
    if request.method == "POST":
        amount_completed = request.POST["amount_completed"]
        new_drill_data = Drill_data(username=request.user,drill_name="Stop",amount_completed=amount_completed)
        new_drill_data.save()
    return render(request,'main_app/Drills/fundamentals/stop.html')

@login_required(login_url='/login/')
def follow(request):
    if request.method == "POST":
        amount_completed = request.POST["amount_completed"]
        new_drill_data = Drill_data(username=request.user,drill_name="Follow",amount_completed=amount_completed)
        new_drill_data.save()
    return render(request,'main_app/Drills/fundamentals/follow.html')

@login_required(login_url='/login/')
def draw(request):
    if request.method == "POST":
        amount_completed = request.POST["amount_completed"]
        new_drill_data = Drill_data(username=request.user,drill_name="Draw",amount_completed=amount_completed)
        new_drill_data.save()
    return render(request,'main_app/Drills/fundamentals/draw.html')

@login_required(login_url='/login/')
def mightyx_stun(request):
    if request.method == "POST":
        amount_completed = request.POST["amount_completed"]
        new_drill_data = Drill_data(username=request.user,drill_name="Mightyx_Stun",amount_completed=amount_completed)
        new_drill_data.save()
    return render(request,'main_app/Drills/fundamentals/mightyx_stun.html')

@login_required(login_url='/login/')
def mightyx_follow(request):
    if request.method == "POST":
        amount_completed = request.POST["amount_completed"]
        new_drill_data = Drill_data(username=request.user,drill_name="Mightyx_Follow",amount_completed=amount_completed)
        new_drill_data.save()
    return render(request,'main_app/Drills/fundamentals/mightyx_follow.html')

@login_required(login_url='/login/')
def mightyx_draw(request):
    if request.method == "POST":
        amount_completed = request.POST["amount_completed"]
        new_drill_data = Drill_data(username=request.user,drill_name="Mightyx_Draw",amount_completed=amount_completed)
        new_drill_data.save()
    return render(request,'main_app/Drills/fundamentals/mightyx_draw.html')

    


#shotmaking
@login_required(login_url='/login/')
def mill(request):
    if request.method == "POST":
        amount_completed = request.POST["amount_completed"]
        new_drill_data = Drill_data(username=request.user,drill_name="The Mill",amount_completed=amount_completed)
        new_drill_data.save()
    return render(request,'main_app/Drills/shotmaking/mill.html')

@login_required(login_url='/login/')
def everest(request):
    if request.method == "POST":
        amount_completed = request.POST["amount_completed"]
        new_drill_data = Drill_data(username=request.user,drill_name="Everest",amount_completed=amount_completed)
        new_drill_data.save()
    return render(request,'main_app/Drills/shotmaking/everest.html')

@login_required(login_url='/login/')
def ladder(request):
    if request.method == "POST":
        amount_completed = request.POST["amount_completed"]

        new_drill_data = Drill_data(username=request.user,drill_name="Ladder",amount_completed=amount_completed)
        new_drill_data.save()
    return render(request,'main_app/Drills/shotmaking/ladder.html')

@login_required(login_url='/login/')
def corner(request):
    if request.method == "POST":
        amount_completed = request.POST["amount_completed"]

        new_drill_data = Drill_data(username=request.user,drill_name="Corner",amount_completed=amount_completed)
        new_drill_data.save()
    return render(request,'main_app/Drills/shotmaking/corner.html')

@login_required(login_url='/login/')
def train (request):
    if request.method == "POST":
        amount_completed = request.POST["amount_completed"]

        new_drill_data = Drill_data(username=request.user,drill_name="Train",amount_completed=amount_completed)
        new_drill_data.save()
    return render(request,'main_app/Drills/shotmaking/train.html')

@login_required(login_url='/login/')
def follower(request):
    if request.method == "POST":
      
        amount_completed = request.POST["amount_completed"]

        new_drill_data = Drill_data(username=request.user,drill_name="Follower",amount_completed=amount_completed)
        new_drill_data.save()
    return render(request,'main_app/Drills/shotmaking/follower.html')

#kicking
@login_required(login_url='/login/')
def one_rail_kick(request):
    if request.method == "POST":
      
        amount_completed = request.POST["amount_completed"]

        new_drill_data = Drill_data(username=request.user,drill_name="One_rail_kick",amount_completed=amount_completed)
        new_drill_data.save()
    return render(request,'main_app/Drills/kicking/one_rail_kick.html')


@login_required(login_url='/login/')
def two_rail_kick(request):
    if request.method == "POST":
      
        amount_completed = request.POST["amount_completed"]

        new_drill_data = Drill_data(username=request.user,drill_name="Two_rail_kick",amount_completed=amount_completed)
        new_drill_data.save()
    return render(request,'main_app/Drills/kicking/two_rail_kick.html')

@login_required(login_url='/login/')
def three_rail_kick(request):
    if request.method == "POST":
      
        amount_completed = request.POST["amount_completed"]

        new_drill_data = Drill_data(username=request.user,drill_name="Three_rail_kick",amount_completed=amount_completed)
        new_drill_data.save()
    return render(request,'main_app/Drills/kicking/three_rail_kick.html')

@login_required(login_url='/login/')
def kicking1(request):
    if request.method == "POST":
      
        amount_completed = request.POST["amount_completed"]

        new_drill_data = Drill_data(username=request.user,drill_name="Kicking1",amount_completed=amount_completed)
        new_drill_data.save()
    return render(request,'main_app/Drills/kicking/kicking1.html')

@login_required(login_url='/login/')
def kicking2(request):
    if request.method == "POST":
      
        amount_completed = request.POST["amount_completed"]

        new_drill_data = Drill_data(username=request.user,drill_name="Kicking2",amount_completed=amount_completed)
        new_drill_data.save()
    return render(request,'main_app/Drills/kicking/kicking2.html')


@login_required(login_url='/login/')
def kicking3(request):
    if request.method == "POST":
      
        amount_completed = request.POST["amount_completed"]

        new_drill_data = Drill_data(username=request.user,drill_name="Kicking3",amount_completed=amount_completed)
        new_drill_data.save()
    return render(request,'main_app/Drills/kicking/kicking3.html')

#banking
@login_required(login_url='/login/')
def one_rail_bank(request):
    if request.method == "POST":
      
        amount_completed = request.POST["amount_completed"]

        new_drill_data = Drill_data(username=request.user,drill_name="One_rail_bank",amount_completed=amount_completed)
        new_drill_data.save()
    return render(request,'main_app/Drills/banking/one_rail_bank.html')

@login_required(login_url='/login/')
def two_rail_bank(request):
    if request.method == "POST":
      
        amount_completed = request.POST["amount_completed"]

        new_drill_data = Drill_data(username=request.user,drill_name="Two_rail_bank",amount_completed=amount_completed)
        new_drill_data.save()
    return render(request,'main_app/Drills/banking/two_rail_bank.html')

@login_required(login_url='/login/')
def three_rail_bank(request):
    if request.method == "POST":
      
        amount_completed = request.POST["amount_completed"]

        new_drill_data = Drill_data(username=request.user,drill_name="Three_rail_bank",amount_completed=amount_completed)
        new_drill_data.save()
    return render(request,'main_app/Drills/banking/three_rail_bank.html')

@login_required(login_url='/login/')
def four_rail_bank(request):
    if request.method == "POST":
      
        amount_completed = request.POST["amount_completed"]

        new_drill_data = Drill_data(username=request.user,drill_name="Four_rail_bank",amount_completed=amount_completed)
        new_drill_data.save()
    return render(request,'main_app/Drills/banking/four_rail_bank.html')

@login_required(login_url='/login/')
def banking1(request):
    if request.method == "POST":
      
        amount_completed = request.POST["amount_completed"]

        new_drill_data = Drill_data(username=request.user,drill_name="Banking1",amount_completed=amount_completed)
        new_drill_data.save()
    return render(request,'main_app/Drills/banking/banking1.html')

@login_required(login_url='/login/')
def banking2(request):
    if request.method == "POST":
      
        amount_completed = request.POST["amount_completed"]

        new_drill_data = Drill_data(username=request.user,drill_name="Banking2",amount_completed=amount_completed)
        new_drill_data.save()
    return render(request,'main_app/Drills/banking/banking2.html')


@login_required(login_url='/login/')
def safety1(request):
    if request.method == "POST":
      
        amount_completed = request.POST["amount_completed"]

        new_drill_data = Drill_data(username=request.user,drill_name="Safety1",amount_completed=amount_completed)
        new_drill_data.save()
    return render(request,'main_app/Drills/safety/safety1.html')

@login_required(login_url='/login/')
def safety2(request):
    if request.method == "POST":
      
        amount_completed = request.POST["amount_completed"]

        new_drill_data = Drill_data(username=request.user,drill_name="Safety2",amount_completed=amount_completed)
        new_drill_data.save()
    return render(request,'main_app/Drills/safety/safety2.html')

@login_required(login_url='/login/')
def safety3(request):
    if request.method == "POST":
      
        amount_completed = request.POST["amount_completed"]

        new_drill_data = Drill_data(username=request.user,drill_name="Safety3",amount_completed=amount_completed)
        new_drill_data.save()
    return render(request,'main_app/Drills/safety/safety3.html')


@login_required(login_url='/login/')
def safety4(request):
    if request.method == "POST":
      
        amount_completed = request.POST["amount_completed"]

        new_drill_data = Drill_data(username=request.user,drill_name="Safety4",amount_completed=amount_completed)
        new_drill_data.save()
    return render(request,'main_app/Drills/safety/safety4.html')

@login_required(login_url='/login/')
def safety5(request):
    if request.method == "POST":
      
        amount_completed = request.POST["amount_completed"]

        new_drill_data = Drill_data(username=request.user,drill_name="Safety5",amount_completed=amount_completed)
        new_drill_data.save()
    return render(request,'main_app/Drills/safety/safety5.html')

@login_required(login_url='/login/')
def safety6(request):
    if request.method == "POST":
      
        amount_completed = request.POST["amount_completed"]

        new_drill_data = Drill_data(username=request.user,drill_name="Safety6",amount_completed=amount_completed)
        new_drill_data.save()
    return render(request,'main_app/Drills/safety/safety6.html')


@login_required(login_url='/login/')
def jumping1(request):
    if request.method == "POST":
      
        amount_completed = request.POST["amount_completed"]

        new_drill_data = Drill_data(username=request.user,drill_name="jumping1",amount_completed=amount_completed)
        new_drill_data.save()
    return render(request,'main_app/Drills/jumping/jumping1.html')

@login_required(login_url='/login/')
def jumping2(request):
    if request.method == "POST":
      
        amount_completed = request.POST["amount_completed"]

        new_drill_data = Drill_data(username=request.user,drill_name="jumping2",amount_completed=amount_completed)
        new_drill_data.save()
    return render(request,'main_app/Drills/jumping/jumping2.html')

@login_required(login_url='/login/')
def jumping3(request):
    if request.method == "POST":
      
        amount_completed = request.POST["amount_completed"]

        new_drill_data = Drill_data(username=request.user,drill_name="jumping3",amount_completed=amount_completed)
        new_drill_data.save()
    return render(request,'main_app/Drills/jumping/jumping3.html')


@login_required(login_url='/login/')
def jumping4(request):
    if request.method == "POST":
      
        amount_completed = request.POST["amount_completed"]

        new_drill_data = Drill_data(username=request.user,drill_name="jumping4",amount_completed=amount_completed)
        new_drill_data.save()
    return render(request,'main_app/Drills/jumping/jumping4.html')

@login_required(login_url='/login/')
def jumping5(request):
    if request.method == "POST":
      
        amount_completed = request.POST["amount_completed"]

        new_drill_data = Drill_data(username=request.user,drill_name="jumping5",amount_completed=amount_completed)
        new_drill_data.save()
    return render(request,'main_app/Drills/jumping/jumping5.html')

@login_required(login_url='/login/')
def jumping6(request):
    if request.method == "POST":
      
        amount_completed = request.POST["amount_completed"]

        new_drill_data = Drill_data(username=request.user,drill_name="jumping6",amount_completed=amount_completed)
        new_drill_data.save()
    return render(request,'main_app/Drills/jumping/jumping6.html')