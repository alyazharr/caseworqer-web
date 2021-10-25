from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ProfilPerusahaan(models.Model):
    companyName = models.CharField(max_length=50)
    companyAddress = models.TextField()
    companyEmail = models.EmailField(max_length=254)
    companyPhoneNumber = models.CharField(max_length=13)
    companyDescription = models.TextField()
    companyOwner = models.CharField(max_length=30)
    
    def __str__(self):
        return self.companyName
