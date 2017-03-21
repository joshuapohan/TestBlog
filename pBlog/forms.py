from django import forms
from django.utils.text import slugify

class PostForm(forms.Form):
    title = forms.CharField(max_length=200)
    message = forms.CharField(widget=forms.Textarea)
