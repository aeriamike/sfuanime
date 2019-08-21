from django.urls import path

from . import views

app_name = 'sfuanime'
urlpatterns = [
    path('', views.index, name='index'),
    path('posts/', views.posts, name='posts'),
    path('events/', views.events, name='events'),
    path('about/', views.about, name='about'),
    path('admins/', views.admins, name='admins'),

]
