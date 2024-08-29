from django.contrib import admin
from .models import Article,Topic, Comment
from django.contrib.auth.models import User

admin.site.register(Article)
admin.site.register(Topic)
admin.site.register(Comment)

