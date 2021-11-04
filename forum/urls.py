from django.urls import path
from . import views

urlpatterns = [
    path('',views.forum, name='forum-post'),
    path('add',views.add_post,name='add-forum'),
    path('<int:forum_pk>/add-comment',views.add_comment,name='add-forum-comment'),
]