from django.shortcuts import render

# Create your views here.
def home_page_func(request):
    return render(request, 'my_app/home_page.html')