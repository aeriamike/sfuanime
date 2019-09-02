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

<<<<<<< HEAD
    return render(request, 'sfuanime/post_index.html',{"postid":postid,"next":next,"length":length, "prev":prev})


def post_tag(request,tag):
    taggy = tag
    posty = Posts.objects.all()

    tag_ans= posty.filter(post_tag__contains = [tag])

    return render(request, 'sfuanime/post_tag.html',{"tag":tag,"tag_ans":tag_ans})


def post_month(request,time):

    year = time[:4]
    month = time[4:]
    print(year)
    print(month)


    dep =Posts.objects.filter(post_date__year = year,post_date__month = month)

    return render(request, 'sfuanime/post_month.html',{"time":time,"dep":dep,"month":month,"year":year})
=======
    if length-1>post_id:
        return render(request, 'sfuanime/index.html', {"posts":posts})

    else:
        return render(request, 'sfuanime/post_index.html',{"postid":postid,"next":next,"length":length, "prev":prev})


def post_tag(request,tag):

    return render(request, 'sfuanime/post_tag.html')


def post_month(request,month):

    return render(request, 'sfuanime/post_month.html')
>>>>>>> 73f157eac73a6ce53f5775d16b5e182438dd4a21



def postmaker(request):

    return render(request, 'sfuanime/postmaker.html')






# Create your views here.
