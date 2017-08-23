from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from ui.forms import RegistrationForm


# Create your views here.
def index(request):
    
    built_context ={ 'user': request.user }
    return render(request, template_name = "ui/index.html", context = built_context)

def getMap(request):
    return render(request, template_name = 'ui/map.html')

def register(request):
    
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('index')
    else:
        form = RegistrationForm()
         
    args = {'form':form}        
     
    return render(request, template_name = 'account/register.html', context = args)
    

def login(request):
    return render(request, template_name = 'account/login.html')
