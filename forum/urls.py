from django.urls import path
from . import views

urlpatterns = [
    path('',views.forum, name='forum-post'),
    path('add',views.add_post,name='add-forum'),
    path('<int:forum_pk>',views.forum,name='add-forum-comment'),
    path('json', views.returnJson, name ='forum-json'),
]