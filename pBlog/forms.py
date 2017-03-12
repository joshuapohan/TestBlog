from django import forms

class PostForm(forms.Form):
    title = forms.CharField(max_length=200)
    user = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
