from django.shortcuts import render
from .models import Posts
from django.http import HttpResponse

def index(request):
    posts = Posts.objects.all()
    print("index")


    return render(request, 'sfuanime/index.html', {"posts":posts})



def posts(request):
    posts = Posts.objects.all()
    print("posts")

    return render(request, 'sfuanime/posts.html', {"posts":posts})



def events(request):
    return render(request, 'sfuanime/events.html')

def about(request):
    return render(request, 'sfuanime/about.html')

def admins(request):
    return render(request, 'sfuanime/admins.html')





# Create your views here.
