from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import DateTimeField
from django.utils import timezone

class PostForum(models.Model):
    title = models.CharField(default=None, max_length=150)
    message = models.TextField()
    postTime = models.DateTimeField(auto_now_add=True)

# class PostComment(models.Model):
#     post = models.ForeignKey('PostForum', on_delete=CASCADE, null=True, blank=True)
#     commentText = models.TextField()
#     commentTime = models.DateTimeField(auto_now_add=True)