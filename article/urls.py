from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('article/<int:pk>', views.article, name='article'),
    path('input/',views.input_data,name='input'),
    path('create_topic/',views.create_topic,name='create_topic'),
    path('create_article/',views.create_article,name='create_article'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)