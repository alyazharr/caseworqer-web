from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class PostForum(models.Model):
    title = models.CharField(default=None, max_length=200)
    message = models.TextField(max_length=1200)
    postTime = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)