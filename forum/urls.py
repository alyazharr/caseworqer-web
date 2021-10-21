from django.urls import path
from .views import forumPost

urlpatterns = [
    path('',forumPost.forum, name='forum-post'),
]