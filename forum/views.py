from django.http import response
from django.shortcuts import render,redirect
from django.views import View
from .models import PostForum, PostComment
from .forms import InputForum, CommentSection


def forum(request, forum_pk=None):
    username = "Unknown"
    if request.user.is_authenticated:
        username = request.user.get_username()
    PostContent = PostForum.objects.all().values().order_by('-postTime')
    CommentContent = PostComment.objects.all().values()
    comment = CommentSection
    response = {
        'author':username,
        'PostContent': PostContent,
        'CommentContent':CommentContent,
        'comment':comment
        }

    if forum_pk != None:
        content_post = PostForum.objects.get(pk=forum_pk)
        if request.method == 'POST':
            postCom = CommentSection(request.POST)
            if postCom.is_valid():
                postCom_new = postCom.save(commit=False)
                postCom_new.post_id = content_post.id
                if username != "Unknown": #if user login
                    postCom_new.userCom = username
                # or it will replace by the username
                postCom.save()
            return redirect('/forum')
    else:
        return render(request, 'forum.html', response)


def add_post(request):
    username = "Unknown"
    if request.user.is_authenticated:
        username = request.user.get_username()
    inputPost = InputForum
    response = {'inputContent':inputPost}
    if request.method == 'POST':
        post = InputForum(request.POST)
        if post.is_valid():
            post_new = post.save(commit=False)
            post_new.userPost = username
            post.save()
        return redirect('/forum')
    return render(request, 'add_forum.html', response)
