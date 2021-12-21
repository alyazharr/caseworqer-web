from django import forms
from django.db.models import fields
from .models import perusahaanKomen

class reviewForm(forms.Form):
    
    description = forms.CharField(
        widget=forms.Textarea
    )

    def save(self, job, user):
        komentar = perusahaanKomen.objects.create(description = self.cleaned_data['description'],
        pekerjaan=job, penulis=user) 

        return komentar
