from django.shortcuts import render,redirect
from django.http import HttpResponse,request
from .models import content
from django.contrib.auth.decorators import login_required
from . import forms
from .models import content

# Create your views here.
def home(request):
    context = content.objects.all()

    return render(request,'article/index.html',{'context':context})

def articleContent(request,aid):
    context = content.objects.filter(id=aid)
    return render(request,'article/article.html',{'context':context[0]})


@login_required(login_url = 'login')
def creat_article(request):
    if request.method == 'POST':    
        form = forms.createArticle(request.POST,request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('home')
    else:
        form = forms.createArticle()
        return render(request,'article/create.html',{'form':form})

    
def like(request,aid,action):

    article = content.objects.get(id=aid)
    if action==1:
        like =article.like
        like = like +1
        article.like = like
        article.save()
        return redirect('content',aid=aid)
    elif action==0:
        like =article.like
        like = like-1
        article.like = like
        article.save()
        return redirect('content',aid=aid)