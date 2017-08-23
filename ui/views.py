from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, template_name = "ui/index.html")

def getMap(request):
    return render(request, template_name = 'ui/map.html')

def register(request):
    return render(request, template_name = 'account/register.html')

def login(request):
    return render(request, template_name = 'account/login.html')
