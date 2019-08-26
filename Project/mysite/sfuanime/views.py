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

def post_index(request, post_id):
    postid = Posts.objects.filter(id = post_id)
    next = post_id + 1
    prev = post_id - 1
    length = len(Posts.objects.all())

    if length-1>post_id:
        return render(request, 'sfuanime/index.html', {"posts":posts})

    else:
        return render(request, 'sfuanime/post_index.html',{"postid":postid,"next":next,"length":length, "prev":prev})


def post_tag(request,tag):

    return render(request, 'sfuanime/post_tag.html')


def post_month(request,month):

    return render(request, 'sfuanime/post_month.html')



def postmaker(request):

    return render(request, 'sfuanime/postmaker.html')






# Create your views here.
