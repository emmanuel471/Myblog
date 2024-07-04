from django.shortcuts import redirect, render
from django.shortcuts import render, get_object_or_404
from .models import Topic, Article

def article(request):
    topics = Topic.objects.all()
    articles = Article.objects.all()

    content = {
        'topics' : topics,
        'articles': articles,
    }
    
    return render(request,'article.html',content)
