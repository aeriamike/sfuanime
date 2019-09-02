from django.urls import path


from . import views

app_name = 'sfuanime'
urlpatterns = [
    path('', views.index, name='index'),
    path('posts/', views.posts, name='posts'),
    path('posts/tag/<str:tag>', views.post_tag, name='post_tag'),
<<<<<<< HEAD
    path('posts/date/<str:time>', views.post_month, name='post_month'),
    path('events/', views.events, name='events'),
    path('about/', views.about, name='about'),
    path('admins/', views.admins, name='admins'),
    path('postmaker/', views.postmaker, name='postmaker'),
    path('posts/<int:post_id>',views.post_index, name="post_index"),
=======
    path('posts/month/<str:month>', views.post_month, name='post_month'),
    path('events/', views.events, name='events'),
    path('about/', views.about, name='about'),
    path('admins/', views.admins, name='admins'),
    path('posts/<int:post_id>',views.post_index, name="post_index"),
    path('postmaker/',views.postmaker, name = "postmaker")
>>>>>>> 73f157eac73a6ce53f5775d16b5e182438dd4a21

]
