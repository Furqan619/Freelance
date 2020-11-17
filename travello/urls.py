from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
      path('', views.index, name='index.html'),
      path('esubscribe', views.esubscribe, name="subscribe"),
      path('contact', views.contact, name="contact"),
      
     
]

