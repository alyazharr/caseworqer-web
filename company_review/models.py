from django.db import models

# Create your models here.
class company_review(models.Model):
    value = models.Value()
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    postTime = models.DateTimeField("date published",auto_now_add=True)