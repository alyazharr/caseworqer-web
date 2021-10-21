from typing import NewType
from django.http import response
from django.shortcuts import render,redirect
from .models import PostForum
from django.views import View
from .forms import InputForum

name = "asajsjaaaskeee"
def forum(request): # ini buat nulis isi boxnya apa aja
    PostContent = PostForum.objects.all().values()
    response = {'PostContent': PostContent}
    return render(request, 'forum.html', response)
    
# ini buat formnya
def add_post(request):
    inputPost = InputForum
    response = {'name':name,'inputContent':inputPost}
    if request.method == 'POST':
        post = InputForum(request.POST)
        if post.is_valid():
            post.save()
            return redirect('forum/')
    return render(request, 'add_forum.html',response)