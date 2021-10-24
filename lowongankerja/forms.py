from main.models import LowonganKerja
from django.forms import ModelForm, fields

class PembukaLowonganForm(ModelForm):
    class Meta:
        model = LowonganKerja
        fields = "__all__"