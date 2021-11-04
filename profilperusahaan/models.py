from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ProfilPerusahaan(models.Model):
    companyName = models.CharField(max_length=50, default="Unknown company name")
    companyAddress = models.TextField(default="Unknown Address")
    companyEmail = models.EmailField(max_length=254, default="Unknown Email")
    companyPhoneNumber = models.CharField(max_length=13, default="Unknown Phone Number")
    companyDescription = models.TextField(default="Unknown Company Description")
    companyOwner = models.CharField(max_length=30, default="UnknownOwner")
    
    def __str__(self):
        return self.companyName
