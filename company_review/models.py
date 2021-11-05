from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields.related import ForeignKey
from main.models import LowonganKerja

# Create your models here.
class perusahaanKomen(models.Model):
    pekerjaan = models.ForeignKey(LowonganKerja, on_delete=models.CASCADE)
    penulis = models.ForeignKey(User, on_delete=models.CASCADE)
    value = models.IntegerField(null = True, blank = True)
    description = models.TextField(max_length=500, null = True, blank = True)
    postTime = models.DateTimeField("date published",auto_now_add=True, null = True, blank = True)

    class Meta:
        unique_together = ('pekerjaan', 'penulis',) 