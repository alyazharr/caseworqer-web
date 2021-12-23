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

@csrf_exempt
def forum(request, forum_pk=None):
    response = {}
    username = "Unknown"

    PostContent = PostForum.objects.all().values().order_by('-postTime')
    CommentContent = PostComment.objects.all().values()

    try :
        get_json_com = json.loads(request.body)
        print(get_json_com)
        inputCom = CommentSection(get_json_com)
        # mengaitkan comment dengan parent dari data yang sudah dikirim json
        if inputCom.is_valid():
            postCom_new = inputCom.save(commit=False)
            postCom_new.post_id = get_json_com['post']
        inputCom.save()
        web = False # jika berasal dari mobile

    except :
        web = True

        # pada web terdapat autentikasi
        if request.user.is_authenticated:
            username = request.user.get_username()
        
        inputCom = CommentSection(request.POST or None)
        
        response['author'] = username
        response['PostContent'] = PostContent
        response['CommentContent'] = CommentContent
        response['comment'] = inputCom

    if inputCom.is_valid() and request.method == 'POST' and web==True:
        if forum_pk != None:
            content_post = PostForum.objects.get(pk=forum_pk)
            if request.method == 'POST':
                inputCom = CommentSection(request.POST)
                if inputCom.is_valid():
                    postCom_new = inputCom.save(commit=False)
                    postCom_new.post_id = content_post.id
                    if username != "Unknown": #if user login
                        postCom_new.userCom = username
                    # or it will replace by the username
                    inputCom.save()
                return redirect('/forum')
        else : 
            return render(request, 'forum.html', response)

    response['comment'] = inputCom
    return render(request, 'forum.html', response)  

@csrf_exempt
def add_post(request):
    response = {}
    try :
        get_json = json.loads(request.body)
        print(get_json)
        inputPost = InputForum(get_json)
        if inputPost.is_valid():
            postCom_new = inputPost.save(commit=False)
            postCom_new.userPost = get_json['userPost']
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


# method pengiriman data json
def post_json(request):
    data_post = serializers.serialize('json', PostForum.objects.all())
    return HttpResponse(data_post, content_type="application/json")

def com_json(request):
    data_com = serializers.serialize('json', PostComment.objects.all())
    return HttpResponse(data_com, content_type="application/json")