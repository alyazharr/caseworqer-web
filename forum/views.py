from typing import NewType
from django.http import response
from django.shortcuts import render,redirect
from .models import PostForum
from django.views import View
from .forms import InputForum

class forumPost(View):
    def forum(request, *args, **kwargs):
        PostContent = PostForum.objects.all().values() .order_by('-postTime')
        inputPost = InputForum()

        response = {
            'PostContent': PostContent,
            'inputContent':inputPost,}

        return render(request, 'forum.html', response)
    
    def add_post(request, *args, **kwargs):
        PostContent = PostForum.objects.all().order_by('-postTime')
        inputPost = InputForum
        response = {
            'PostContent': PostContent,
            'inputContent':inputPost,
        }
        if request.method == 'POST':
            post = InputForum(request.POST)
            if post.is_valid():
                post.save()
                return redirect('/forum')

        return render(request, 'forum.html', response)

    
    # def add_post(request, *args, **kwargs):
    #     PostContent = PostForum.objects.all().values() .order_by('-postTime')
    #     inputPost = InputForum(request.POST)

    #     response = {
    #         'PostContent': PostContent,
    #         'inputContent':inputPost,
    #     }
        
    #     if inputPost.is_valid():
    #         new_post = inputPost.save(commit=False)
    #         new_post.author = request.user
    #         new_post.save()
            
    #     return render(request, 'forum.html', response)

