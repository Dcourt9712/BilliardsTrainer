from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request,'main_app/home.html')

def index(request):
    return render(request, 'main_app/form.html')

def search(request):
    return render(request, 'main_app/form.html')

def submit(request):
    search_id = request.POST.get('textfield', None)
    print(search_id)
    if request.method == 'POST':
        search_id = request.POST.get('textfield', None)
        try:
            user = search_id
            #do something with user
            html = (f'<H1>{user}</H1>')
            return HttpResponse(html)
        except (search_id == None or search_id == ''):
            print("bad response")
            response = ("<H1>Bad Input</H1> <H2><a href='main_app/form.html'>Go back</a><H2>")
            return HttpResponse(response)  
    else:
        return render(request, 'main_app/form.html')