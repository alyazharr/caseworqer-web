from django import forms
from django.forms import ModelForm
from .models import PostForum

class InputForum(forms.ModelForm):
    title = forms.CharField(
        widget=forms.Textarea(attrs={
            'rows':'2',
            'placeholder':'Write Your Forum Title Here ...',
        })
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={
            'rows':'12',
            'placeholder':'Write Your Post Here ...',
        })
    )
    class Meta :
        model = PostForum
        fields = ['title','message']