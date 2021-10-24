from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from main.models import Pelamar

# Create your models here.
class ProfilPerusahaan(models.Model):
    companyName = models.CharField(max_length=50)
    companyAddress = models.TextField()
    companyEmail = models.EmailField(max_length=254)
    companyPhoneNumber = models.CharField(max_length=13)
    companyDescription = models.TextField()

    # One [perusahaan] to Many [pelamar] relations
    #companyApplicant = models.ForeignKey(Pelamar, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.companyName
