from django.http import response
from django.shortcuts import render,redirect
from django.views import View
# from .models import PostForum, PostComment
from .models import PostForum
# from .forms import InputForum, CommentSection
from .forms import InputForum


def forum(request): # ini buat nulis isi boxnya apa aja
    username = None
    if request.user.is_authenticated:
        username = request.user.get_username()
    PostContent = PostForum.objects.all().values().order_by('-postTime')
    # CommentContent = PostComment.objects.all().values()
    # response = {'author':username,'PostContent': PostContent,'CommentContent':CommentContent}
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
    return render(request, 'add_forum.html', response)

# # ini buat pass pk
# def replybtn(request, forum_pk):
#     content_post = PostForum.objects.get(pk=forum_pk)
#     content_com = CommentSection(request.POST)
#     if content_com.is_valid():
#         new_com = content_com.save(commit=False)
#         new_com.post_id = content_post.id
#         new_com.save()
#         return redirect('/add-comment',pk=forum_pk)
#     return render(request, 'add_comment.html')

# # ini buat comment
# def add_comment(request, forum_pk):
#     content_post = PostForum.objects.get(pk=forum_pk)
#     comment = CommentSection
#     response = {'comment':comment}
#     if request.method == 'POST':
#         postCom = CommentSection(request.POST)
#         if postCom.is_valid():
#             postCom_new = postCom.save(commit=False)
#             postCom_new.post_id = content_post.id
#             postCom.save()
#             return redirect('/forum')
#     return render(request, 'add_comment.html',response)