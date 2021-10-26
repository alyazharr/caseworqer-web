from django.db import models
from django.db.models.fields import CharField
from django.urls import reverse
# Create your models here.
class Tipskarier(models.Model):
    
    Title = models.CharField(max_length= 100)
    Article = models.TextField()
    Cover = models.ImageField(null = True,blank=True, upload_to="images/")


    
    def get_absolute_url(self):
        return reverse('tipskarier:tipskarier')
    
 