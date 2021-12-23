from django.db.models import expressions
from django.http import response
from django.shortcuts import render,redirect
from django.http.response import HttpResponse
from django.views import View
from django.http import JsonResponse
from .models import PostForum, PostComment
from django.core import serializers 
from .forms import InputForum, CommentSection
from django.views.decorators.csrf import csrf_exempt
import json

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

@csrf_exempt
def add_post(request):
    username = "Unknown"
    response = {}
    try :
        get_json = json.loads(request.body)
        print(get_json)
        inputPost = InputForum(get_json)
        post_new = inputPost.save(commit=False)
        post_new.userPost = username
        inputPost.save()
        web = False
    except :
        if request.user.is_authenticated:
            username = request.user.get_username()
        inputPost = InputForum(request.POST or None)
        web = True
    
    if inputPost.is_valid() and request.method == 'POST' and web==True:
        post_new = inputPost.save(commit=False)
        post_new.userPost = username
        inputPost.save()
        return redirect('/forum')

    response['inputContent'] = inputPost
    return render(request, 'add_forum.html', response)

def post_json(request):
    data_post = serializers.serialize('json', PostForum.objects.all())
    return HttpResponse(data_post, content_type="application/json")

def com_json(request):
    data_com = serializers.serialize('json', PostComment.objects.all())
    return HttpResponse(data_com, content_type="application/json")