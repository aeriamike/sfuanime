from django.urls import path


from . import views

app_name = 'sfuanime'
urlpatterns = [
    path('', views.index, name='index'),
    path('posts/', views.posts, name='posts'),
    path('posts/tag/<str:tag>', views.post_tag, name='post_tag'),
    path('posts/month/<str:month>', views.post_month, name='post_month'),
    path('events/', views.events, name='events'),
    path('about/', views.about, name='about'),
    path('admins/', views.admins, name='admins'),
    path('posts/<int:post_id>',views.post_index, name="post_index"),
    path('postmaker/',views.postmaker, name = "postmaker")

]
