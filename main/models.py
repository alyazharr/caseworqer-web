from django.db import models

# Create your models here.
class LowonganKerja(models.Model):
    jobs = models.CharField(max_length=50)
    company = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    jobType = models.CharField(max_length=10)
    about = models.TextField()

class Pelamar(models.Model):
    nama = models.CharField(max_length=50)
    usia = models.IntegerField()
    pendidikan = models.CharField(max_length=20)
    alamat = models.TextField()
    email = models.EmailField(max_length = 254)
    jenisKelamin = models.CharField(max_length = 10)
    sertifikatVaksin = models.TextField()
    idLowongan = models.IntegerField(blank=True,null=True)
