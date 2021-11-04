from django.db import models
from django.db.models.fields import CharField
from django.urls import reverse
from ckeditor.fields import RichTextField

# Create your models here.
class Tipskarier(models.Model):
    
    Title = models.CharField(max_length= 100)
    Article = RichTextField(blank= True, null = True)
    Cover = models.ImageField(null = True,blank=True, upload_to="static/images/tipskarier/")
    Summary = models.TextField(max_length= 500, null = True)
    Highlight = models.IntegerField(blank= True, null = True)


    
    def get_absolute_url(self):
        return reverse('tipskarier:tipskarier')
    
    def __str__(self):
        return self.Title
 
