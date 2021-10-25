from django import forms
from django.db.models import fields
from django import forms
from .models import company_review
from django.forms import ModelForm

class reviewForm(ModelForm):
    
    name = forms.CharField(
        widget=forms.TextInput
    )

    description = forms.CharField(
        widget=forms.Textarea
    )

    class Meta:
        model = company_review
        fields = "__all__"