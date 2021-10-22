from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class PostForum(models.Model):
    title = models.CharField(default=None, max_length=150)
    message = models.TextField()
    postTime = models.DateTimeField("date published",auto_now_add=True)
    def __str__(self):
        return self.title
