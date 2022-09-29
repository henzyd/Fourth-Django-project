from cProfile import label
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms.models import ModelForm
from . import models

mychioce = [('alex', 'alex'), ('uche', 'uche'), ('bolu', 'bolu')]
class SignUpForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


# NOTE this is for creating forms
# class CreateForm(forms.Form):
#     name = forms.CharField(max_length=100, required=True, label='my_test_form')
#     email = forms.EmailField()
#     random = forms.CharField(widget= forms.Textarea())
#     chioce = forms.CharField(widget=forms.Select(choices=mychioce), label='stuff')


# NOTE this is for creating post
class CreatePostForm(ModelForm):
    class Meta:
        model = models.Post
        fields = ['user_title', 'user_body']