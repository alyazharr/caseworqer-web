from django import forms
from django.forms import widgets
from .models import Tipskarier

class TipsForm(forms.ModelForm):
    class Meta:
        model  = Tipskarier
        fields = ('Title','Article','Cover')

        error_messages = {
            'required':'Please Type/ upload'
        }
        input_attrs = {
            'type':'text',
            'placeholder': 'Judul artikel''Masukkan Artikel'
            
        }
        widgets = {
            'Title' : forms.TextInput(attrs = input_attrs),
            'Article': forms.TextInput(attrs= input_attrs),
            
        }
        # Title = forms.CharField(label="",required = False, max_length = 30,widget= forms.TextInput(attrs = input_attrs))
        # Article = forms.CharField(label="",required = False, max_length = 30,widget= forms.TextInput(attrs = input_attrs))
        # File = forms.ImageField(widget= forms.I)
        