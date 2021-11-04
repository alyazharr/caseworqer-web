from django import forms
from django.forms import widgets
from .models import Tipskarier


class TipsForm(forms.ModelForm):
    class Meta:
        model  = Tipskarier
        fields = ('Title','Summary','Article','Cover','Highlight')

        error_messages = {
            'required':'Please Type/ upload'
        }

        widgets = {
            'Title' : forms.TextInput(attrs = {'class': 'form-control','placeholder': 'Judul artikel'}),
            'Article': forms.Textarea(attrs= {'class': 'form-control','placeholder': 'Masukkan Artikel'}),
            'Summary':forms.Textarea(attrs = {'class': 'form-control','placeholder': 'Masukkan Ringkasan (max: 100 kata)','id': 'id_message1'}),
            'Highlight' : forms.NumberInput(attrs = {'class': 'form-control','placeholder': 'Masukkan angka 0 atau 1 (2 untuk pioritas)'})
        }
   
class EditForm(forms.ModelForm):
    class Meta:
        model  = Tipskarier
        fields = ('Title','Summary','Article','Cover','Highlight')

        error_messages = {
            'required':'Please Type/ upload'
        }
        widgets = {
            'Title' : forms.TextInput(attrs = {'class': 'form-control','placeholder': 'Judul artikel'}),
            'Article': forms.Textarea(attrs= {'class': 'form-control','placeholder': 'Masukkan Artikel'}),
            'Summary':forms.Textarea(attrs = {'class': 'form-control','placeholder': 'Masukkan Ringkasan (max: 100 kata)','id': 'id_message1'}),
            'Highlight' : forms.NumberInput(attrs = {'class': 'form-control','placeholder': 'Masukkan angka 0 atau 1 (2 untuk pioritas)'})
        }