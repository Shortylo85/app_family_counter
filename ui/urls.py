
from django.conf.urls import url, include
from django.contrib import admin

from ui import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^map/$', views.getMap, name='getMap'),
    url(r'^login/$', views.login, name='login'),
    url(r'^register/$', views.register, name='register'),

    
]
