from django.http import response
from django.shortcuts import render,redirect
from django.http.response import HttpResponse
from django.views import View
from django.http import JsonResponse
from .models import PostForum, PostComment
from django.core import serializers 
from .forms import InputForum, CommentSection
from django.views.decorators.csrf import csrf_exempt


data_post = []

def forum(request, forum_pk=None):
    username = "Unknown"
    if request.user.is_authenticated:
        username = request.user.get_username()
    PostContent = PostForum.objects.all().values().order_by('-postTime')
    CommentContent = PostComment.objects.all().values()
    comment = CommentSection
    returnJson()    
    response = {
        'author':username,
        'PostContent': PostContent,
        'CommentContent':CommentContent,
        'comment':comment,
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

def returnJson(request):
    PostContent = PostForum.objects.all().values().order_by('-postTime')
    CommentContent = PostComment.objects.all().values()
    flag = False
    for i in PostContent :
        for k in data_post:
            if(i['id'] == k['id']):
                flag = True
        if (not flag) :
            each = {
                'id': i['id'],
                'field' : {
                    'title' : i['title'],
                    'message' : i['message'],
                    'time' : i['postTime'],
                    'user' : i['userPost'],
                    'comment' : []
                }
            }
            for j in CommentContent :
                if i['id']==j['post_id']:
                    tiap = {
                        'idCom' : j['id'],
                        'fieldCom': {
                        'textCom':j['commentText'],
                        'dateCom':j['commentTime'],
                        'userCom':j['userCom'] 
                        }
                    }
                    each['field']['comment'].append(tiap)
            data_post.append(each)
    result = data_post
    return JsonResponse(result, safe=False)
