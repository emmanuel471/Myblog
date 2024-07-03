from django.contrib import admin
from django.urls import path
from . import views



urlpatterns = [
    path('', views.home, name='home'),
    path('admin/',views.admin, name='admin'),
    path('about/', views.about, name='about'),  
]
