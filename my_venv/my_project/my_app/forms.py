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


# class CreateForm(forms.Form):
#     name = forms.CharField(max_length=100)
#     email = forms.EmailField()
#     random = forms.CharField(widget= forms.Textarea())


class CreatePostForm(ModelForm):
    class Meta:
        model = models.Post
        fields = ['user_title', 'user_body', 'user_date_created', 'user_owner']