from django.shortcuts import redirect, render
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse

def article(request):
    return render(request, 'article.html')

# Create your views here.
