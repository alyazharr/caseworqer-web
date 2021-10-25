from django.urls import path
from .views import cardStar

urlpatterns = [
    path('',cardStar, name='forum-post'),
]