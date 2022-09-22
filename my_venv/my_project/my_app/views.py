from django.shortcuts import render, redirect
from . import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from . import forms

# Create your views here.
def home_page_func(request):
    posts = models.Post.objects.all()
    last = models.Post.objects.all().last()
    print(posts)
    context = {
        'posts': posts,
        'last_post': last
    }
    return render(request, 'my_app/home_page.html', context)


def about_page_func(request):
    posts = models.Post.objects.all()[0]
    return render(request, 'my_app/about_page.html', {'posts': posts})

def signup_page_func(request):
    if request.method == 'POST':
        form = forms.SignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            form.save()
            messages.success(request, f'Hello {username}, your account has been created successfully')
            return redirect('home_page')
    else:
        form = forms.SignUpForm()
        
    return render(request, 'my_app/signup_page.html', {'form': form})

def details_page_func(request, pk):
    posts = models.Post.objects.all().filter(id=pk)[0]
    return render(request, 'my_app/about_page.html', {'posts': posts})


# def test_forms(request):
#     form = forms.CreateForm()
#     return render(request, 'my_app/test_form.html', {'form': form})


def create_post_forms(request):
    form = forms.CreatePostForm()
    return render(request, 'my_app/test_form.html', {'form': form})