from django.contrib import admin
from .models import Category,Profile, Education, Project
from django.contrib.auth.models import User

admin.site.register(Category)
admin.site.register(Education)
admin.site.register(Profile)
admin.site.register(Project)
