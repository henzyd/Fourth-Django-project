from django.urls import path
from my_app import views as my_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', my_views.home_page_func, name = 'home_page'),
    path('about/', my_views.about_page_func, name = 'about_page'),
    path('register/', my_views.signup_page_func, name = 'signup_page'),
    path('create-post/', my_views.create_post_forms, name = 'create-forms'),
    path('item/<int:pk>', my_views.details_page_func, name = 'details_page'),
    path('login/', auth_views.LoginView.as_view(template_name = 'my_app/login_page.html'), name = 'login_page'),
    path('logout/', auth_views.LogoutView.as_view(template_name = 'my_app/logout_page.html'), name = 'logout_page'),
]