from typing import Optional
from django.db import models
from django.db.models.fields import DateTimeField
from django.utils import timezone

class PostForum(models.Model):
    title = models.CharField(default=None, max_length=150)
    message = models.TextField()
    postTime = models.DateTimeField("date published",auto_now_add=True)