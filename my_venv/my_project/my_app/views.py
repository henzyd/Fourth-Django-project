from django.shortcuts import render, redirect
from . import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from . import forms
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# Create your views here.
def home_page_func(request):
    posts = models.Post.objects.all()
    last = models.Post.objects.all().last()
    # print(posts)
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


def test_forms(request):
    form = forms.CreateForm()
    return render(request, 'my_app/test_form.html', {'form': form})

@login_required
def create_post_forms(request):
    user = request.user
    if request.method == 'POST':
        form = forms.CreatePostForm(request.POST)
        if form.is_valid():
            form_title = form.cleaned_data.get('user_title')
            form_body = form.cleaned_data.get('user_body')
            models.Post.objects.create(user_title=form_title, user_body=form_body, user_owner=user)
            messages.success(request, f'Post created')
            return redirect('home_page')
    else:
        form = forms.CreatePostForm()
        
    return render(request, 'my_app/test_form.html', {'form': form})


class PostListView(ListView):
    model = models.Post
    context_object_name = 'posts'


class PostDetailView(DetailView):
    model = models.Post 
    # context_object_name = 'goat'


class ClassCreatePost(LoginRequiredMixin, CreateView):
    model = models.Post
    fields = ['user_title', 'user_body']

    def form_valid(self, form):
        form.instance.user_owner = self.request.user ##### NOTE this is the same as - user = request.user
        return super().form_valid(form) ##### NOTE this is the same as - form.is_valid()


class ClassUpdatePost(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = models.Post
    fields = ['user_title', 'user_body']

    def form_valid(self, form):
        form.instance.user_owner = self.request.user ##### NOTE this is the same as - user = request.user
        return super().form_valid(form) ##### NOTE this is the same as - form.is_valid()

    def test_func(self): #### this returns a bool
        post = self.get_object()
        if post.user_owner == self.request.user:
            return True
        else:
            return False


class ClassDeletePost(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = models.Post
    success_url = '/'
    
    def test_func(self): #### this returns a bool
        post = self.get_object()
        if post.user_owner == self.request.user:
            return True
        else:
            return False
    

####### NOTE this is using a function based view to do what was done above
def postdelete(request, pk):
    user = request.user
    if models.Post.objects.filter(id = pk).exists():
        print("object exists")
        post = models.Post.objects.filter(id = pk).first()
        if user == post.owner: 
            print("user ownership verified")
            models.Post.objects.get(id = pk).delete()
            messages.success(request, 'Post Deleted')
            return redirect('homepage')
        else:
            print("ownership not verified")
            messages.success(request, "You cant delete this post")
            return redirect('homepage')       
    else:
        print("object does not exist")
        messages.success(request, "Post does not exist")
        return redirect('homepage')

