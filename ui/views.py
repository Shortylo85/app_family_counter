from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Index")

def getMap(request):
    return HttpResponse("getMap")

def register(request):
    return HttpResponse("Register")

def login(request):
    return HttpResponse("Login")
