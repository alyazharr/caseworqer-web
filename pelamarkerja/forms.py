from main.models import Pelamar
from django.forms import ModelForm

class PelamarForm(ModelForm):
    class Meta:
        model = Pelamar
        fields = ['nama', 'usia', 'pendidikan','alamat', 'email', 'jenisKelamin', 'sertifikatVaksin','idLowongan']