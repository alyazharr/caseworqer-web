from django.http import response
from django.shortcuts import render,redirect
from django.views import View
from .models import PostForum
from .forms import InputForum
import requests

def forum(request): # ini buat nulis isi boxnya apa aja
    username = None
    if request.user.is_authenticated:
        username = request.user.get_username()
    PostContent = PostForum.objects.all().values().order_by('-postTime')
    response = {'author':username,'PostContent': PostContent}
    return render(request, 'forum.html', response)
    
# ini buat formnya
def add_post(request):
    inputPost = InputForum
    response = {'inputContent':inputPost}
    if request.method == 'POST':
        post = InputForum(request.POST)
        if post.is_valid():
            post.save()
            return redirect('/forum')
    return render(request, 'add_forum.html',response)