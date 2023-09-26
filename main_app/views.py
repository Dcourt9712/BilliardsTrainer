from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request,'main_app/home.html')

def drills(request):
    drills = {'1':"Images/billiards.jpg",}
    
   
    return render(request,'main_app/drills.html',drills)
