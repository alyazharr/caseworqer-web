from django.urls import path
from .views import forumPost

urlpatterns = [
    path('',forumPost.as_view(), name='forum-post'),
]