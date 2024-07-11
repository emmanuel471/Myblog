from django.contrib import messages
from django.shortcuts import redirect, render
from django.shortcuts import render, get_object_or_404
from .models import Topic, Article
from .forms import ArticleForm, InputForm, MyForm, TopicForm

def article(request, pk):
    articles = Article.objects.get(id=pk)

    content = {
        'articles': articles,
    }
    
    return render(request,'article.html',content)


def input_data(request):
    form = InputForm()
    if request.method == 'POST':
        form = InputForm(request.POST)

        context = {
                'form' : form
                }

        if form.is_valid():
            print('form valid')
            return render(request,'input.html',context)
        else:
            return render(request,'error_404.html')    
    return render(request,'input.html',{'form':form})
 
 
def create_topic(request):
    if request.method == 'POST':
        form = TopicForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Topic created successfully!')
            return redirect('home') 
        else:
            return render(request, 'error_404.html', {'form': form})
    else:
        form = TopicForm()
    return render(request, 'create_topic.html', {'form': form})

def create_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.save()
            messages.success(request, 'Article created successfully!')
            return redirect('home') 
    else:
        form = ArticleForm()
    return render(request, 'create_article.html', {'form': form})

def error_404(request):
    form = MyForm(request.POST or None)
    if request.method == 'POST' and not form.is_valid():
        return render(request, 'error_404.html', {'form': form})
    return render(request, 'error_404.html')