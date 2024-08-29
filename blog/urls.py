from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('', views.home, name='home'),
    path('admin/',views.admin, name='admin'),
    path('about/', views.about, name='about'), 
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
