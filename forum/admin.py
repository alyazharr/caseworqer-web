from django.contrib import admin
from .models import PostForum, PostComment

admin.site.register(PostForum)
admin.site.register(PostComment)