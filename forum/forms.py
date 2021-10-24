from django import forms
from django.forms import ModelForm
from .models import PostForum

class InputForum(forms.ModelForm):
    title = forms.CharField(
        label='Post Title',
        widget=forms.Textarea(attrs={
            'rows':'2',
            'placeholder':'What\'s Your Forum Title ?',
        })
    )
    message = forms.CharField(
        label='Post Message',
        widget=forms.Textarea(attrs={
            'rows':'10',
            'placeholder':'Write Your Post Here ...',
        })
    )
    class Meta :
        model = PostForum
        fields = ['title','message']