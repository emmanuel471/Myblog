from django.contrib import messages
from django.shortcuts import redirect, render
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.conf import settings
from  article.models import Article, Topic
from .models import Project, Profile, Education, Category
from django.core.mail import EmailMessage
from django.core.mail import send_mail
import logging

logger = logging.getLogger(__name__)


# Create your views here.
def home(request):
    topics = Topic.objects.all()
    
    context = {
        'topics': topics,
    }
    return render(request, 'index.html', context)

def about(request):
    projects = Project.objects.all()
    qualifs = Education.objects.all()
    profiles = Profile.objects.all()
    categories = Category.objects.all()
    
    # Get the first profile, if it exists
    profile = profiles.first() if profiles.exists() else None
    

    # Group qualifications by category
    category_qualifs = {}
    for category in categories:
        category_qualifs[category] = qualifs.filter(category=category)
    
    content = {
        'projects': projects,
        'category_qualifs': category_qualifs,
        'profile': profile,
    }
    return render(request, 'about.html', content)

def admin(request):
	return render(request, 'admin.html')

