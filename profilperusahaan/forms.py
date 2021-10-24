from .models import ProfilPerusahaan
from django.forms import ModelForm

class ProfilPerusahaanForm(ModelForm):
    class Meta:
        model = ProfilPerusahaan
        fields = ['companyName','companyAddress','companyEmail','companyPhoneNumber','companyDescription']