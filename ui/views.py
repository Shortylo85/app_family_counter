from django.contrib.auth import login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from ui.forms import RegistrationForm
from ui.models import City


# Create your views here.
def index(request):
    
    built_context ={ 'user': request.user }
    return render(request, template_name = "ui/index.html", context = built_context)

def getMap(request):
    
    cities = City.objects.filter(city_name = 'New York')
#     
#     print(cities.city_name)
    
    built_context = {
        'cities': cities,
    }
    
    return render(request, template_name = 'ui/map.html', context = built_context)

def register(request):
    
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid:
            form.save()
            user = User.objects.last()
            login(request, user)
            return redirect('index')
    else:
        form = RegistrationForm()
         
    args = {'form':form}        
     
    return render(request, template_name = 'account/register.html', context = args)
    
# 
# def login(request):
#      
#     return render(request, template_name = 'account/login.html')
