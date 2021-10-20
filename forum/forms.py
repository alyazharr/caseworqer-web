from django import forms
from django.db.models import fields
from .models import PostForum

class InputForum(forms.ModelForm):
    message = forms.CharField(
        label='',
        widget=forms.Textarea(attrs={
            'rows':'3',
            'placeholder':'Write Your Post Here ...'
        })
    )
    class Meta :
        model = PostForum
        fields = ['message']