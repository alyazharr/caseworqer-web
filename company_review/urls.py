from django.urls import path
from .views import cardStar, read_job

urlpatterns = [
    path('',cardStar, name='forum-post'),
    path('job/<str:id_job>', read_job, name='read_job')
]