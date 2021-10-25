from django import forms
from django.contrib.auth.models import User
from .models import ProfilPerusahaan

# membuat ModelForm
class ProfilPerusahaanForm(forms.ModelForm):
    class Meta:
        model = ProfilPerusahaan # model yang digunakan
        fields = "__all__" # semua fields di model ProfilPerusahaan harus digunakan