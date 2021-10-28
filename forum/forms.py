from django import forms
from django.forms import ModelForm, fields
from .models import PostForum, PostComment

class InputForum(forms.ModelForm):
    title = forms.CharField(
        label='Post Title',
        widget=forms.Textarea(attrs={
            'rows':'1','cols':'65',
            'style':'font-size:15px',
            'placeholder':'What\'s Your Forum Title ?',
        })
    )
    message = forms.CharField(
        label='Post Message',
        widget=forms.Textarea(attrs={
            'rows':'10', 'cols':'65',
            'placeholder':'Write Your Post Here ...',
            'style':'font-size:15px'
        })
    )
    class Meta :
        model = PostForum
        fields = ['title','message']

class CommentSection(forms.ModelForm):
    commentText = forms.CharField(
        label='',
        widget=forms.Textarea(attrs={
            'rows':'4', 'cols':'65',
            'placeholder':'Write Your Comment Here ...',
            'style':'font-size:15px'
        })
    )
    class Meta :
        model = PostComment
        fields = ['commentText']