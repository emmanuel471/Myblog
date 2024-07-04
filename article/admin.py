from django.contrib import admin
from .models import Article,Topic
from django.contrib.auth.models import User

admin.site.register(Article)
admin.site.register(Topic)

