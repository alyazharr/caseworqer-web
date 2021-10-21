from django import forms
from django.forms import ModelForm
from django.db.models import fields
from .models import PostForum

class InputForum(ModelForm):
    message = forms.CharField(
        label='ariariaira',
        widget=forms.Textarea(attrs={
            'rows':'3',
            'placeholder':'Write Your Post Here ...'
        })
    )
    class Meta :
        model = PostForum
        fields = ('message',)