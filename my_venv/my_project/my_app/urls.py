from django.urls import path
from my_app import views as my_views
from django.contrib.auth import views as auth_views

######### Media files
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', my_views.home_page_func, name = 'home_page'),
    path('about/', my_views.about_page_func, name = 'about_page'),
    path('register/', my_views.signup_page_func, name = 'signup_page'),
    # path('register/', my_views.test_forms, name = 'signup_page'),
    path('create-post/', my_views.create_post_forms, name = 'create_forms'),
    path('item/<int:pk>/', my_views.details_page_func, name = 'details_page'),
    path('login/', auth_views.LoginView.as_view(template_name = 'my_app/login_page.html'), name = 'login_page'),
    path('logout/', auth_views.LogoutView.as_view(template_name = 'my_app/logout_page.html'), name = 'logout_page'),
    
    ######### NOTE this is the class based view 
    path('plist/', my_views.PostListView.as_view(template_name = 'my_app/plist.html'), name = 'plist_page'),
    path('plist-detail/<int:pk>/', my_views.PostDetailView.as_view(template_name = 'my_app/plist_detail.html'), name='plist_detail_page'), 
    path('class-create-post/', my_views.ClassCreatePost.as_view(template_name = 'my_app/class_create_post_form.html'), name = 'class_create_post_page'),
    path('update-post/<int:pk>/', my_views.ClassUpdatePost.as_view(template_name = 'my_app/update_post_form.html'), name = 'update_post_page'),
    path('delete-post/<int:pk>/', my_views.ClassDeletePost.as_view(template_name = 'my_app/delete_post_form.html'), name = 'delete_post_page'),
    # path('funcdelete/<int:pk>/', my_views.postdelete, name='func_delete'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  