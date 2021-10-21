from django.urls import path
from . import views

urlpatterns = [
    path('',views.forum, name='forum-post'),
    path('add',views.add_post,name='add-forum'),
]